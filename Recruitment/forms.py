from django import forms
from . import models

class JobCreationForm(forms.ModelForm):
    class Meta:
        job_choice = [("Full Time", "Full Time"), ("Part Time", "Part Time"), ("Freelance", "Freelance"),
                      ("Internship", "Internship"), ("Temporary", "Temporary")]
    
        model = models.Job
        fields = ['title', 'company', 'job_type', 'location', 'description', 'salary', 'vacancies', 'open']
        labels = {
            'title':'Job title',
            'company':'Firm offering',
            'job_type':'Job Type',
            'location':'Job location',
            'description':"Job Description",
            'open':"Is the Job open for Applications"
        }
        widgets = {
            'title': forms.TextInput(attrs={'id':"fullname", 'name':'title','placeholder': 'eg. Professional UI/UX Designer', 'class':'form-control'}),
            'company': forms.TextInput(attrs={'id':"fullname", 'name':'company', 'placeholder': 'e.g KMC', 'class':'form-control'}),
            'location': forms.TextInput(attrs={'placeholder': 'e.g Kampala', 'name':'location', 'class':'form-control'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Job Description', 'name':'description', 'rows': 5, 'cols': 30, 'class':'form-control'}),
            'job_type': forms.Select(choices=job_choice, attrs={'placeholder':'Select From Dropdown', 'name':'job-type', 'class':'form-control w-100'}),
            'salary': forms.TextInput(attrs={'id':"fullname", 'name':'salary', 'placeholder': 'e.g 500,000/=', 'class':'form-control'}),
            'vacancies': forms.NumberInput(attrs={'id':"fullname", 'name':'vacancies', 'placeholder': 'e.g 10', 'class':'form-control'})
        }

class DetailedApplicationForm(forms.ModelForm):
    class Meta:
        model = models.Candidate
        fields = ['first_name', 'last_name', 'middle_name', 'location', 'email', 'contact',
                  'education_background', 'key_competences', 'field_knowledge',
                  'related_experience', 'cv', 'transcript', 'other_files']
        labels = {
            'first_name': "First Name", 'last_name': "Last Name", 'middle_name': "Middle Name",
                     'location': "Your Location", 'email': "Your Email", 'contact': "Your contacts",
            'education_background': "Education background", 'key_competences': "Key competences",
                     'field_knowledge': "Field knowledge",
            'related_experience': "Related experience", 'cv':"Your CV or Resume",
                     'transcript': "Your Transcript", 'other_files': "Other Documents"
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={'name': 'first-name', 'placeholder': 'eg. Stephen',
                       'class': 'form-control'}),
            'middle_name': forms.TextInput(
                attrs={'name': 'middle name', 'placeholder': 'eg. John',
                       'class': 'form-control'}),
            'last_name': forms.TextInput(
                attrs={'name': 'last-name', 'placeholder': 'e.g Paul', 'class': 'form-control'}),
            'location': forms.TextInput(
                attrs={'placeholder': 'e.g Kampala', 'name': 'location', 'class': 'form-control'}),
            'email': forms.EmailInput(
                attrs={'placeholder': 'e.g name@services.com', 'name': 'email', 'class': 'form-control'}),
            'contact': forms.TextInput(
                attrs={'placeholder': 'e.g 0777777777/0756565656', 'name': 'contact', 'class': 'form-control'}),
            'education_background': forms.Textarea(
                attrs={'placeholder': 'Education Background', 'name': 'education', 'rows': 5, 'cols': 30,
                       'class': 'form-control'}),
            'key_competences': forms.Textarea(
                attrs={'placeholder': 'Key competences', 'name': 'competences', 'rows': 5, 'cols': 30,
                       'class': 'form-control'}),
            'field_knowledge': forms.Textarea(
                attrs={'placeholder': 'Field Knowledge', 'name': 'field-knowledge', 'rows': 5, 'cols': 30,
                       'class': 'form-control'}),
            'related_experience': forms.Textarea(
                attrs={'placeholder': 'Related Experience', 'name': 'related-experience', 'rows': 5, 'cols': 30,
                       'class': 'form-control'}),
            "cv": forms.FileInput(
                attrs={'placeholder': 'Resume', 'name': 'cv', 'class': 'form-control'}),
            "transcript": forms.FileInput(
                attrs={'placeholder': 'Transcript', 'name': 'transcript', 'class': 'form-control'}),
            "other_files": forms.FileInput(
                attrs={'placeholder': 'other files', 'name': 'other-files', 'class': 'form-control'})

        }
