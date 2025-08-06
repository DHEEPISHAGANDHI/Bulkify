from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.urls import reverse
from .models import Job, JobApplication, SavedJob
from .forms import JobApplicationForm, SaveJobForm

# Create your views here.

def job_list(request):
    """Display a list of active job postings with search and pagination"""
    search_query = request.GET.get('search', '')
    location_filter = request.GET.get('location', '')
    
    jobs = Job.objects.filter(is_active=True)
    
    # Apply search filters
    if search_query:
        jobs = jobs.filter(
            Q(title__icontains=search_query) | 
            Q(company_name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    if location_filter:
        jobs = jobs.filter(location__icontains=location_filter)
    
    # Pagination
    paginator = Paginator(jobs, 10)  # Show 10 jobs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get unique locations for filter dropdown
    locations = Job.objects.filter(is_active=True).values_list('location', flat=True).distinct()
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'location_filter': location_filter,
        'locations': locations,
        'total_jobs': jobs.count(),
    }
    
    return render(request, 'jobs/job_list.html', context)

def job_detail(request, job_id):
    """Display detailed view of a specific job"""
    job = get_object_or_404(Job, id=job_id, is_active=True)
    
    context = {
        'job': job,
    }
    
    return render(request, 'jobs/job_detail.html', context)

def home(request):
    """Home page with featured jobs"""
    featured_jobs = Job.objects.filter(is_active=True)[:6]  # Show 6 recent jobs
    total_jobs = Job.objects.filter(is_active=True).count()
    
    context = {
        'featured_jobs': featured_jobs,
        'total_jobs': total_jobs,
    }
    
    return render(request, 'jobs/home.html', context)


def apply_job(request, job_id):
    """Handle job application form"""
    job = get_object_or_404(Job, id=job_id, is_active=True)
    
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            
            # Check if user already applied
            if JobApplication.objects.filter(job=job, email=application.email).exists():
                messages.error(request, 'You have already applied for this job with this email address.')
                return render(request, 'jobs/apply_job.html', {'form': form, 'job': job})
            
            application.save()
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('job_detail', job_id=job.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = JobApplicationForm()
    
    context = {
        'form': form,
        'job': job,
    }
    
    return render(request, 'jobs/apply_job.html', context)


def save_job(request, job_id):
    """Save a job for later viewing"""
    if request.method == 'POST':
        job = get_object_or_404(Job, id=job_id, is_active=True)
        email = request.POST.get('email')
        
        if email:
            saved_job, created = SavedJob.objects.get_or_create(
                job=job,
                user_email=email
            )
            
            if created:
                return JsonResponse({
                    'status': 'success',
                    'message': 'Job saved successfully!'
                })
            else:
                return JsonResponse({
                    'status': 'info',
                    'message': 'Job is already saved.'
                })
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Email is required to save jobs.'
            })
    
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method.'
    })


def share_job(request, job_id):
    """Generate shareable link for a job"""
    job = get_object_or_404(Job, id=job_id, is_active=True)
    
    # Generate full URL for sharing
    job_url = request.build_absolute_uri(reverse('job_detail', args=[job.id]))
    
    share_data = {
        'title': f"{job.title} at {job.company_name}",
        'description': job.get_short_description(),
        'url': job_url,
        'location': job.location,
    }
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'success',
            'data': share_data
        })
    
    return render(request, 'jobs/share_job.html', {
        'job': job,
        'share_data': share_data
    })


def saved_jobs(request):
    """Display saved jobs for a user"""
    email = request.GET.get('email', '')
    saved_jobs_list = []
    
    if email:
        saved_jobs_list = SavedJob.objects.filter(user_email=email).select_related('job')
    
    context = {
        'saved_jobs': saved_jobs_list,
        'email': email,
    }
    
    return render(request, 'jobs/saved_jobs.html', context)
