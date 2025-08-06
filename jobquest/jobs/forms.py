from django import forms
from .models import JobApplication, SavedJob


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'first_name', 'last_name', 'email', 'phone_number',
            'resume', 'cover_letter', 'experience_years',
            'linkedin_url', 'portfolio_url', 'current_salary',
            'expected_salary', 'availability_date', 'willing_to_relocate',
            'additional_info'
        ]
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your last name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your.email@example.com'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+1 (555) 123-4567'
            }),
            'resume': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.doc,.docx'
            }),
            'cover_letter': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Write a brief cover letter explaining why you are interested in this position...'
            }),
            'experience_years': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 50
            }),
            'linkedin_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://linkedin.com/in/yourprofile'
            }),
            'portfolio_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://yourportfolio.com'
            }),
            'current_salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': '50000.00'
            }),
            'expected_salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': '60000.00'
            }),
            'availability_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'willing_to_relocate': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'additional_info': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Any additional information you would like to share...'
            }),
        }
        
        labels = {
            'first_name': 'First Name *',
            'last_name': 'Last Name *',
            'email': 'Email Address *',
            'phone_number': 'Phone Number *',
            'resume': 'Resume/CV',
            'cover_letter': 'Cover Letter',
            'experience_years': 'Years of Experience *',
            'linkedin_url': 'LinkedIn Profile',
            'portfolio_url': 'Portfolio Website',
            'current_salary': 'Current Salary (USD)',
            'expected_salary': 'Expected Salary (USD)',
            'availability_date': 'Available Start Date *',
            'willing_to_relocate': 'Willing to Relocate',
            'additional_info': 'Additional Information',
        }


class SaveJobForm(forms.ModelForm):
    class Meta:
        model = SavedJob
        fields = ['user_email']
        widgets = {
            'user_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email to save this job'
            })
        }
