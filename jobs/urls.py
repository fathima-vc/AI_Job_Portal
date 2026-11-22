
from django.urls import path
from . import views

urlpatterns = [

    # Job seeker pages
    path('', views.job_list, name='job_list'),

    path('<int:job_id>/', views.job_detail, name='job_detail'),

    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),

    path('my-applications/', views.my_applications, name='my_applications'),

    # Recruiter dashboard
    path('recruiter-dashboard/', views.recruiter_dashboard, name='recruiter_dashboard'),

    # Post, edit and delete jobs
    path('post-job/', views.post_job, name='post_job'),

    path('edit-job/<int:job_id>/', views.edit_job, name='edit_job'),

    path('delete-job/<int:job_id>/', views.delete_job, name='delete_job'),

    # Applicant management
    path('job/<int:job_id>/applicants/', views.view_applicants, name='view_applicants'),

    path('application/<int:application_id>/update-status/', views.update_application_status, name='update_application_status'),

]
