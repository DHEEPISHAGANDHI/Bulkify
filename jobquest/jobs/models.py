from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=200, help_text="Job title")
    company_name = models.CharField(max_length=150, help_text="Name of the hiring company")
    description = models.TextField(help_text="Detailed job description")
    location = models.CharField(max_length=150, help_text="Job location (city, state, remote, etc.)")
    posting_date = models.DateTimeField(default=timezone.now, help_text="Date when job was posted")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, help_text="Whether the job posting is active")
    
    class Meta:
        ordering = ['-posting_date']
        verbose_name = "Job"
        verbose_name_plural = "Jobs"
    
    def __str__(self):
        return f"{self.title} at {self.company_name}"
    
    def get_short_description(self):
        """Return a truncated version of the description for display"""
        if len(self.description) > 200:
            return self.description[:200] + "..."
        return self.description


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    cover_letter = models.TextField(blank=True)
    experience_years = models.PositiveIntegerField(help_text="Years of relevant experience")
    linkedin_url = models.URLField(blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)
    current_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    expected_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    availability_date = models.DateField(help_text="When can you start?")
    willing_to_relocate = models.BooleanField(default=False)
    additional_info = models.TextField(blank=True, help_text="Any additional information")
    applied_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-applied_at']
        unique_together = ['job', 'email']  # Prevent duplicate applications
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job.title}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class SavedJob(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user_email = models.EmailField()  # Simple email-based saving for now
    saved_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['job', 'user_email']
        ordering = ['-saved_at']
    
    def __str__(self):
        return f"{self.user_email} saved {self.job.title}"
