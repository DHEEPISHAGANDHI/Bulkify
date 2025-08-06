from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from datetime import timedelta
from .models import Job


class JobModelTest(TestCase):
    """Unit tests for the Job model"""
    
    def setUp(self):
        """Set up test data"""
        self.job_data = {
            'title': 'Software Engineer',
            'company_name': 'Tech Company',
            'description': 'Join our team as a software engineer...',
            'location': 'San Francisco, CA',
            'posting_date': timezone.now(),
            'is_active': True
        }
    
    def test_job_creation(self):
        """Test basic job creation"""
        job = Job.objects.create(**self.job_data)
        
        self.assertEqual(job.title, 'Software Engineer')
        self.assertEqual(job.company_name, 'Tech Company')
        self.assertEqual(job.location, 'San Francisco, CA')
        self.assertTrue(job.is_active)
        self.assertIsNotNone(job.created_at)
        self.assertIsNotNone(job.updated_at)
    
    def test_job_str_method(self):
        """Test the __str__ method of Job model"""
        job = Job.objects.create(**self.job_data)
        expected_str = f"{job.title} at {job.company_name}"
        self.assertEqual(str(job), expected_str)
    
    def test_job_default_values(self):
        """Test default values for job fields"""
        job = Job.objects.create(
            title='Test Job',
            company_name='Test Company',
            description='Test description',
            location='Test Location'
        )
        
        self.assertTrue(job.is_active)  # Should default to True
        self.assertIsNotNone(job.posting_date)  # Should have default value
        self.assertIsNotNone(job.created_at)
        self.assertIsNotNone(job.updated_at)
    
    def test_job_ordering(self):
        """Test that jobs are ordered by posting_date descending"""
        older_job = Job.objects.create(
            title='Old Job',
            company_name='Old Company',
            description='Old job description',
            location='Old Location',
            posting_date=timezone.now() - timedelta(days=5)
        )
        
        newer_job = Job.objects.create(
            title='New Job',
            company_name='New Company',
            description='New job description',
            location='New Location',
            posting_date=timezone.now()
        )
        
        jobs = Job.objects.all()
        self.assertEqual(jobs.first(), newer_job)
        self.assertEqual(jobs.last(), older_job)
    
    def test_get_short_description(self):
        """Test the get_short_description method"""
        # Test with short description
        short_desc = "This is a short description."
        job1 = Job.objects.create(
            title='Job 1',
            company_name='Company 1',
            description=short_desc,
            location='Location 1'
        )
        self.assertEqual(job1.get_short_description(), short_desc)
        
        # Test with long description
        long_desc = "This is a very long description " * 20  # > 200 chars
        job2 = Job.objects.create(
            title='Job 2',
            company_name='Company 2',
            description=long_desc,
            location='Location 2'
        )
        short_result = job2.get_short_description()
        self.assertEqual(len(short_result), 203)  # 200 chars + "..."
        self.assertTrue(short_result.endswith("..."))
    
    def test_job_fields_max_length(self):
        """Test field max length constraints"""
        # Test title max length (200)
        long_title = "A" * 200
        job = Job.objects.create(
            title=long_title,
            company_name='Company',
            description='Description',
            location='Location'
        )
        self.assertEqual(len(job.title), 200)
        
        # Test company_name max length (150)
        long_company = "B" * 150
        job.company_name = long_company
        job.save()
        self.assertEqual(len(job.company_name), 150)
        
        # Test location max length (150)
        long_location = "C" * 150
        job.location = long_location
        job.save()
        self.assertEqual(len(job.location), 150)


class JobViewsTest(TestCase):
    """Integration tests for Job views"""
    
    def setUp(self):
        """Set up test data and client"""
        self.client = Client()
        
        # Create test jobs
        self.job1 = Job.objects.create(
            title='Frontend Developer',
            company_name='TechCorp',
            description='Frontend development position with React...',
            location='San Francisco, CA',
            posting_date=timezone.now() - timedelta(days=1)
        )
        
        self.job2 = Job.objects.create(
            title='Backend Developer',
            company_name='DataCorp',
            description='Backend development position with Python...',
            location='New York, NY',
            posting_date=timezone.now() - timedelta(days=2)
        )
        
        self.job3 = Job.objects.create(
            title='Data Scientist',
            company_name='AI Company',
            description='Data science position with machine learning...',
            location='Remote',
            posting_date=timezone.now() - timedelta(days=3),
            is_active=False  # Inactive job
        )
    
    def test_home_view(self):
        """Test the home page view"""
        response = self.client.get(reverse('home'))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Job Quest')
        self.assertContains(response, 'Find Your Dream Career')
        
        # Check that featured jobs are displayed (should show active jobs only)
        self.assertContains(response, self.job1.title)
        self.assertContains(response, self.job2.title)
        self.assertNotContains(response, self.job3.title)  # Inactive job
        
        # Check context variables
        self.assertIn('featured_jobs', response.context)
        self.assertIn('total_jobs', response.context)
        self.assertEqual(response.context['total_jobs'], 2)  # Only active jobs
    
    def test_job_list_view(self):
        """Test the job list page view"""
        response = self.client.get(reverse('job_list'))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Browse Job Opportunities')
        
        # Check that active jobs are listed
        self.assertContains(response, self.job1.title)
        self.assertContains(response, self.job2.title)
        self.assertNotContains(response, self.job3.title)  # Inactive job
        
        # Check context variables
        self.assertIn('page_obj', response.context)
        self.assertIn('total_jobs', response.context)
        self.assertEqual(response.context['total_jobs'], 2)
    
    def test_job_list_search_functionality(self):
        """Test search functionality in job list"""
        # Search by title
        response = self.client.get(reverse('job_list'), {'search': 'Frontend'})
        self.assertContains(response, self.job1.title)
        self.assertNotContains(response, self.job2.title)
        
        # Search by company
        response = self.client.get(reverse('job_list'), {'search': 'DataCorp'})
        self.assertContains(response, self.job2.title)
        self.assertNotContains(response, self.job1.title)
        
        # Search by description
        response = self.client.get(reverse('job_list'), {'search': 'Python'})
        self.assertContains(response, self.job2.title)
        self.assertNotContains(response, self.job1.title)
    
    def test_job_list_location_filter(self):
        """Test location filtering in job list"""
        response = self.client.get(reverse('job_list'), {'location': 'San Francisco, CA'})
        
        self.assertContains(response, self.job1.title)
        self.assertNotContains(response, self.job2.title)
        
        # Test with non-existent location
        response = self.client.get(reverse('job_list'), {'location': 'Nonexistent'})
        self.assertNotContains(response, self.job1.title)
        self.assertNotContains(response, self.job2.title)
    
    def test_job_list_pagination(self):
        """Test pagination in job list"""
        # Create more jobs to test pagination
        for i in range(15):  # Create 15 more jobs (total 17 with existing)
            Job.objects.create(
                title=f'Job {i}',
                company_name=f'Company {i}',
                description=f'Description {i}',
                location=f'Location {i}'
            )
        
        # Test first page
        response = self.client.get(reverse('job_list'))
        self.assertEqual(response.status_code, 200)
        page_obj = response.context['page_obj']
        self.assertEqual(len(page_obj), 10)  # Should show 10 jobs per page
        self.assertTrue(page_obj.has_next())
        
        # Test second page
        response = self.client.get(reverse('job_list'), {'page': 2})
        self.assertEqual(response.status_code, 200)
        page_obj = response.context['page_obj']
        self.assertEqual(len(page_obj), 7)  # Remaining jobs
        self.assertFalse(page_obj.has_next())
    
    def test_job_detail_view(self):
        """Test job detail page view"""
        response = self.client.get(reverse('job_detail', args=[self.job1.id]))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.job1.title)
        self.assertContains(response, self.job1.company_name)
        self.assertContains(response, self.job1.location)
        self.assertContains(response, self.job1.description)
        
        # Check context
        self.assertEqual(response.context['job'], self.job1)
    
    def test_job_detail_view_inactive_job(self):
        """Test job detail view with inactive job returns 404"""
        response = self.client.get(reverse('job_detail', args=[self.job3.id]))
        self.assertEqual(response.status_code, 404)
    
    def test_job_detail_view_nonexistent_job(self):
        """Test job detail view with non-existent job returns 404"""
        response = self.client.get(reverse('job_detail', args=[999]))
        self.assertEqual(response.status_code, 404)


class JobViewsIntegrationTest(TestCase):
    """Integration tests for complete user workflows"""
    
    def setUp(self):
        """Set up test data"""
        self.client = Client()
        
        # Create a variety of test jobs
        self.jobs = []
        job_data = [
            {
                'title': 'Senior Software Engineer',
                'company_name': 'Google',
                'description': 'Senior position requiring 5+ years experience...',
                'location': 'Mountain View, CA'
            },
            {
                'title': 'Junior Developer',
                'company_name': 'Microsoft',
                'description': 'Entry level position for new graduates...',
                'location': 'Seattle, WA'
            },
            {
                'title': 'Product Manager',
                'company_name': 'Apple',
                'description': 'Lead product development and strategy...',
                'location': 'Cupertino, CA'
            },
            {
                'title': 'DevOps Engineer',
                'company_name': 'Amazon',
                'description': 'Manage infrastructure and deployment...',
                'location': 'Remote'
            }
        ]
        
        for data in job_data:
            job = Job.objects.create(**data)
            self.jobs.append(job)
    
    def test_complete_user_journey(self):
        """Test complete user journey from home to job detail"""
        # 1. Visit home page
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Browse All Jobs')
        
        # 2. Navigate to job listings
        response = self.client.get(reverse('job_list'))
        self.assertEqual(response.status_code, 200)
        
        # 3. Search for specific job
        response = self.client.get(reverse('job_list'), {'search': 'Senior'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Senior Software Engineer')
        
        # 4. View job detail
        senior_job = Job.objects.get(title='Senior Software Engineer')
        response = self.client.get(reverse('job_detail', args=[senior_job.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Senior Software Engineer')
        self.assertContains(response, 'Google')
    
    def test_search_and_filter_workflow(self):
        """Test search and filter functionality workflow"""
        # Search by company
        response = self.client.get(reverse('job_list'), {'search': 'Google'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total_jobs'], 1)
        
        # Filter by location
        response = self.client.get(reverse('job_list'), {'location': 'Remote'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total_jobs'], 1)
        
        # Combined search and filter
        response = self.client.get(reverse('job_list'), {
            'search': 'Engineer',
            'location': 'Mountain View, CA'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total_jobs'], 1)
    
    def test_responsive_design_elements(self):
        """Test that responsive design elements are present"""
        response = self.client.get(reverse('home'))
        
        # Check for responsive meta tag
        self.assertContains(response, 'viewport')
        
        # Check for CSS classes that should be present
        self.assertContains(response, 'container')
        self.assertContains(response, 'hero')
        self.assertContains(response, 'nav-menu')
    
    def test_navigation_links(self):
        """Test navigation links work correctly"""
        # Test home navigation
        response = self.client.get(reverse('home'))
        self.assertContains(response, reverse('home'))
        self.assertContains(response, reverse('job_list'))
        
        # Test job list navigation
        response = self.client.get(reverse('job_list'))
        self.assertContains(response, reverse('home'))
        
        # Test breadcrumb navigation in job detail
        job = self.jobs[0]
        response = self.client.get(reverse('job_detail', args=[job.id]))
        self.assertContains(response, reverse('home'))
        self.assertContains(response, reverse('job_list'))


class JobModelQueryTest(TestCase):
    """Test database queries and model methods"""
    
    def setUp(self):
        """Create test data"""
        # Create active jobs
        for i in range(5):
            Job.objects.create(
                title=f'Active Job {i}',
                company_name=f'Company {i}',
                description=f'Description {i}',
                location=f'Location {i}',
                is_active=True
            )
        
        # Create inactive jobs
        for i in range(3):
            Job.objects.create(
                title=f'Inactive Job {i}',
                company_name=f'Inactive Company {i}',
                description=f'Inactive Description {i}',
                location=f'Inactive Location {i}',
                is_active=False
            )
    
    def test_active_jobs_query(self):
        """Test querying only active jobs"""
        active_jobs = Job.objects.filter(is_active=True)
        self.assertEqual(active_jobs.count(), 5)
        
        for job in active_jobs:
            self.assertTrue(job.is_active)
    
    def test_inactive_jobs_query(self):
        """Test querying inactive jobs"""
        inactive_jobs = Job.objects.filter(is_active=False)
        self.assertEqual(inactive_jobs.count(), 3)
        
        for job in inactive_jobs:
            self.assertFalse(job.is_active)
    
    def test_search_functionality(self):
        """Test search query functionality"""
        # Create specific test job
        test_job = Job.objects.create(
            title='Python Developer',
            company_name='Django Corp',
            description='Work with Django framework and Python',
            location='San Francisco, CA'
        )
        
        # Test title search
        results = Job.objects.filter(title__icontains='Python')
        self.assertIn(test_job, results)
        
        # Test company search
        results = Job.objects.filter(company_name__icontains='Django')
        self.assertIn(test_job, results)
        
        # Test description search
        results = Job.objects.filter(description__icontains='Django')
        self.assertIn(test_job, results)
    
    def test_location_filtering(self):
        """Test location filtering functionality"""
        sf_job = Job.objects.create(
            title='SF Job',
            company_name='SF Company',
            description='Job in San Francisco',
            location='San Francisco, CA'
        )
        
        ny_job = Job.objects.create(
            title='NY Job',
            company_name='NY Company',
            description='Job in New York',
            location='New York, NY'
        )
        
        # Test exact location filter
        sf_results = Job.objects.filter(location='San Francisco, CA')
        self.assertIn(sf_job, sf_results)
        self.assertNotIn(ny_job, sf_results)
        
        # Test partial location filter
        ca_results = Job.objects.filter(location__icontains='CA')
        self.assertIn(sf_job, ca_results)
        self.assertNotIn(ny_job, ca_results)


class JobTemplateTest(TestCase):
    """Test template rendering and context"""
    
    def setUp(self):
        """Set up test data"""
        self.client = Client()
        self.job = Job.objects.create(
            title='Template Test Job',
            company_name='Template Company',
            description='Testing template rendering',
            location='Test Location'
        )
    
    def test_base_template_elements(self):
        """Test that base template elements are present"""
        response = self.client.get(reverse('home'))
        
        # Check for essential HTML structure
        self.assertContains(response, '<!DOCTYPE html>')
        self.assertContains(response, '<html lang="en">')
        self.assertContains(response, '<head>')
        self.assertContains(response, '<body>')
        
        # Check for navigation
        self.assertContains(response, 'Job Quest')
        self.assertContains(response, 'nav')
        
        # Check for footer
        self.assertContains(response, 'footer')
        
        # Check for CSS and fonts
        self.assertContains(response, 'static/css/style.css')
        self.assertContains(response, 'Inter')
    
    def test_job_card_template_rendering(self):
        """Test job card rendering in templates"""
        response = self.client.get(reverse('home'))
        
        # Check for job card elements
        self.assertContains(response, self.job.title)
        self.assertContains(response, self.job.company_name)
        self.assertContains(response, self.job.location)
        
        # Check for icons
        self.assertContains(response, 'fas fa-')
    
    def test_pagination_template_rendering(self):
        """Test pagination template rendering"""
        # Create enough jobs to trigger pagination
        for i in range(15):
            Job.objects.create(
                title=f'Pagination Job {i}',
                company_name=f'Pagination Company {i}',
                description=f'Testing pagination {i}',
                location=f'Location {i}'
            )
        
        response = self.client.get(reverse('job_list'))
        
        # Check for pagination elements
        self.assertContains(response, 'pagination')
        self.assertContains(response, 'Page ')
    
    def test_empty_state_template(self):
        """Test empty state template rendering"""
        # Delete all jobs
        Job.objects.all().delete()
        
        response = self.client.get(reverse('job_list'))
        
        # Check for empty state
        self.assertContains(response, 'No jobs found')
        self.assertContains(response, 'empty-state')


if __name__ == '__main__':
    import django
    django.setup()
    
    # Run specific test
    from django.test.utils import get_runner
    from django.conf import settings
    
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["jobs.tests"])
    
    if failures:
        print(f"\n{failures} test(s) failed")
    else:
        print("\nAll tests passed!")
