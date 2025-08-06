from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from .models import Job

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
