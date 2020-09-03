from django.db import models
import re
from django.db.models.signals import pre_save

# Create your models here.
def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        name = instance.name
        name = name.lower()
        slug = re.sub(r' +', '-', name)
        instance.slug = slug

class Job(models.Model):
    slug = models.SlugField(null=True, blank=True, help_text="A short description of the Job",
                            max_length=100, unique=True)
    title = models.CharField(max_length=200, help_text='job title')
    company = models.CharField(max_length=100, help_text='company offering')
    job_type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True, help_text='date and time of job creation')
    open = models.BooleanField(default=True)
    salary = models.CharField(max_length=20)
    vacancies = models.IntegerField()

    def __str__(self):
        return self.title

class Candidate(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    location =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=50)
    education_background = models.TextField()
    key_competences = models.TextField()
    field_knowledge = models.TextField()
    related_experience = models.TextField()
    cv = models.FileField(upload_to='cvs/', null=True, blank=True)
    transcript = models.FileField(upload_to='transcripts/', null=True, blank=True)
    other_files = models.FileField(upload_to='other_docs/', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, help_text='date and time of application')

    def __str__(self):
        return self.first_name + self.last_name


pre_save.connect(slug_generator, sender=Job)