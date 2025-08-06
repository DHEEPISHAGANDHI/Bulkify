from django.contrib import admin
from .models import Job


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
