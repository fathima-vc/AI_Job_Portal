
from django import forms
from .models import Job, JobApplication


# Form for creating and editing jobs
class JobForm(forms.ModelForm):

    class Meta:
        model = Job

        fields = [
            'title',
            'company',
            'location',
            'description',
            'requirements',
            'salary',
            'job_type',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter job title'
            }),

            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter company name'
            }),

            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter job location'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe the job'
            }),

            'requirements': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter job requirements'
            }),

            'salary': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter salary'
            }),

            'job_type': forms.Select(attrs={
                'class': 'form-control'
            }),
        }


# Form for updating application status
class ApplicationStatusForm(forms.ModelForm):

    class Meta:
        model = JobApplication

        fields = ['status']

        widgets = {
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
