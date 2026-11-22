from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Job, JobApplication
from .forms import JobForm, ApplicationStatusForm


# Display all active jobs
def job_list(request):

    jobs = Job.objects.filter(
        is_active=True
    ).order_by('-created_at')

    search_query = request.GET.get('search', '').strip()

    if search_query:
        jobs = jobs.filter(
            Q(title__icontains=search_query) |
            Q(company__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(requirements__icontains=search_query)
        )

    return render(request, 'jobs/job_list.html', {
        'jobs': jobs,
        'search_query': search_query
    })


# Display job details
def job_detail(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id,
        is_active=True
    )

    already_applied = False

    if request.user.is_authenticated:
        already_applied = JobApplication.objects.filter(
            job=job,
            applicant=request.user
        ).exists()

    return render(request, 'jobs/job_detail.html', {
        'job': job,
        'already_applied': already_applied
    })


# Apply for a job
@login_required
def apply_job(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id,
        is_active=True
    )

    if request.method == 'POST':

        cover_letter = request.POST.get('cover_letter', '')

        application, created = JobApplication.objects.get_or_create(
            job=job,
            applicant=request.user,
            defaults={'cover_letter': cover_letter}
        )

        if created:
            messages.success(
                request,
                'Your application was submitted successfully!'
            )
        else:
            messages.info(
                request,
                'You have already applied for this job.'
            )

        return redirect('job_list')

    return render(request, 'jobs/apply.html', {
        'job': job
    })


# View my applications
@login_required
def my_applications(request):

    applications = JobApplication.objects.filter(
        applicant=request.user
    ).select_related('job').order_by('-applied_at')

    return render(request, 'jobs/my_applications.html', {
        'applications': applications
    })


# Recruiter dashboard
@login_required
def recruiter_dashboard(request):

    if request.user.role != 'recruiter':
        messages.error(
            request,
            'Only recruiters can access this page.'
        )
        return redirect('job_list')

    jobs = Job.objects.filter(
        recruiter=request.user
    ).order_by('-created_at')

    return render(request, 'jobs/recruiter_dashboard.html', {
        'jobs': jobs
    })


# Post a new job
@login_required
def post_job(request):

    if request.user.role != 'recruiter':
        messages.error(
            request,
            'Only recruiters can post jobs.'
        )
        return redirect('job_list')

    if request.method == 'POST':

        form = JobForm(request.POST)

        if form.is_valid():

            job = form.save(commit=False)
            job.recruiter = request.user
            job.save()

            messages.success(
                request,
                'Job posted successfully!'
            )

            return redirect('recruiter_dashboard')

    else:
        form = JobForm()

    return render(request, 'jobs/post_job.html', {
        'form': form
    })


# Edit a job
@login_required
def edit_job(request, job_id):

    if request.user.role != 'recruiter':
        messages.error(request, 'Only recruiters can edit jobs.')
        return redirect('job_list')

    job = get_object_or_404(
        Job,
        id=job_id,
        recruiter=request.user
    )

    if request.method == 'POST':

        form = JobForm(request.POST, instance=job)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Job updated successfully!'
            )

            return redirect('recruiter_dashboard')

    else:
        form = JobForm(instance=job)

    return render(request, 'jobs/edit_job.html', {
        'form': form,
        'job': job
    })


# Delete a job
@login_required
def delete_job(request, job_id):

    if request.user.role != 'recruiter':
        messages.error(request, 'Only recruiters can delete jobs.')
        return redirect('job_list')

    job = get_object_or_404(
        Job,
        id=job_id,
        recruiter=request.user
    )

    if request.method == 'POST':

        job.delete()

        messages.success(
            request,
            'Job deleted successfully!'
        )

        return redirect('recruiter_dashboard')

    return render(request, 'jobs/delete_job.html', {
        'job': job
    })


# View applicants for a recruiter's job
@login_required
def view_applicants(request, job_id):

    if request.user.role != 'recruiter':
        messages.error(request, 'Only recruiters can view applicants.')
        return redirect('job_list')

    job = get_object_or_404(
        Job,
        id=job_id,
        recruiter=request.user
    )

    applications = JobApplication.objects.filter(
        job=job
    ).select_related('applicant').order_by('-applied_at')

    return render(request, 'jobs/view_applicants.html', {
        'job': job,
        'applications': applications
    })


# Update an applicant's status
@login_required
def update_application_status(request, application_id):

    if request.user.role != 'recruiter':
        messages.error(request, 'Only recruiters can update application status.')
        return redirect('job_list')

    application = get_object_or_404(
        JobApplication,
        id=application_id,
        job__recruiter=request.user
    )

    if request.method == 'POST':

        form = ApplicationStatusForm(
            request.POST,
            instance=application
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Application status updated successfully!'
            )

        else:
            messages.error(
                request,
                'Please select a valid application status.'
            )

    return redirect(
        'view_applicants',
        job_id=application.job.id
    )
