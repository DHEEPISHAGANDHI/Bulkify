from django.contrib import admin
from .models import Job, JobApplication, SavedJob


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    """Admin configuration for Job model"""
    
    list_display = ('title', 'company_name', 'location', 'posting_date', 'is_active')
    list_filter = ('is_active', 'posting_date', 'location', 'company_name')
    search_fields = ('title', 'company_name', 'description', 'location')
    list_editable = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Job Information', {
            'fields': ('title', 'company_name', 'description', 'location')
        }),
        ('Status & Dates', {
            'fields': ('is_active', 'posting_date', 'created_at', 'updated_at')
        }),
    )
    
    date_hierarchy = 'posting_date'
    ordering = ('-posting_date',)
    
    def get_queryset(self, request):
        """Optimize admin queries"""
        return super().get_queryset(request).select_related()


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    """Admin configuration for JobApplication model"""
    
    list_display = ('full_name', 'job', 'email', 'experience_years', 'applied_at')
    list_filter = ('applied_at', 'experience_years', 'willing_to_relocate', 'job__company_name')
    search_fields = ('first_name', 'last_name', 'email', 'job__title', 'job__company_name')
    readonly_fields = ('applied_at',)
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number')
        }),
        ('Job Information', {
            'fields': ('job', 'applied_at')
        }),
        ('Professional Details', {
            'fields': ('experience_years', 'current_salary', 'expected_salary', 'availability_date', 'willing_to_relocate')
        }),
        ('Documents & Links', {
            'fields': ('resume', 'linkedin_url', 'portfolio_url')
        }),
        ('Application Details', {
            'fields': ('cover_letter', 'additional_info'),
            'classes': ('collapse',)
        }),
    )
    
    date_hierarchy = 'applied_at'
    ordering = ('-applied_at',)
    
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = 'Full Name'


@admin.register(SavedJob)
class SavedJobAdmin(admin.ModelAdmin):
    """Admin configuration for SavedJob model"""
    
    list_display = ('user_email', 'job', 'saved_at')
    list_filter = ('saved_at', 'job__company_name')
    search_fields = ('user_email', 'job__title', 'job__company_name')
    readonly_fields = ('saved_at',)
    
    date_hierarchy = 'saved_at'
    ordering = ('-saved_at',)
