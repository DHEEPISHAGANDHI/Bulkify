from django.db import models
from django.utils import timezone

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
