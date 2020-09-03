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
