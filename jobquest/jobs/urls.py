from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
    path('jobs/<int:job_id>/apply/', views.apply_job, name='apply_job'),
    path('jobs/<int:job_id>/save/', views.save_job, name='save_job'),
    path('jobs/<int:job_id>/share/', views.share_job, name='share_job'),
    path('saved-jobs/', views.saved_jobs, name='saved_jobs'),
]