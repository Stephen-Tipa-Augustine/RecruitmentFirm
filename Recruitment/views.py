from django.shortcuts import render, redirect, get_object_or_404
from . import forms, models
import re

# Create your views here.

def index(request):
    # This returns an ordered list by date field
    jobs = [models.Job.objects.order_by('date')[i] for i in range(len(models.Job.objects.order_by('date')) - 1, -1, -1)]
    recentJobs = jobs[ : 10]
    col1, col2, col3, col4 = None, None, None, None
    if len(jobs) % 4 == 0:
        n = int(len(jobs)/4)
        col1 = jobs[:n]; col2 = jobs[n:2*n]; col3 = jobs[2*n:3*n]; col4 = jobs[3*n:4*n]
    else:
        r1 = len(jobs) % 4
        n = int((len(jobs) - r1) / 4)
        col1 = jobs[:n]; col2 = jobs[n:2 * n]; col3 = jobs[2 * n:3 * n]; col4 = jobs[3 * n:4 * n]
        if r1 % 3 == 0:
            col1.append(jobs[-3])
            col2.append(jobs[-2])
            col3.append(jobs[-1])
        elif r1 % 2 == 0:
            col1.append(jobs[-2])
            col2.append(jobs[-1])
        else:
            col1.append(jobs[-1])
    context = {'jobs':jobs, 'recentJobs':recentJobs, 'col1':col1, 'col2':col2, 'col3':col3, 'col4':col4}
    return render(request, 'recruitment/index.html', context=context)

def job_query(request):
    if request.method == 'POST':
        job_title = request.POST.get("job-title")
        job_type = request.POST.get("job-type")
        location = request.POST.get("location")
        query_result = None
        if job_title == '' and location == '' and job_type != '':
            query_result = models.Job.objects.filter(job_type=job_type)
        elif job_type == '' and job_title == '' and location != '':
            query_result = models.Job.objects.filter(location=location)
        elif job_type != '' and job_title == '' and location != '':
            query_result = models.Job.objects.filter(location=location, job_type=job_type)
        elif job_title != '' and job_type == '' and location == '':
            jobs = models.Job.objects.all()
            query_result = [i for i in jobs if re.search(job_title, i.title)]
        elif job_title != '' and job_type != '' and location != '':
            jobs = models.Job.objects.filter(job_type=job_type, location=location)
            query_result = [i for i in jobs if re.search(job_title, i.title)]
        elif job_title != '' and job_type != '' and location == '':
            jobs = models.Job.objects.filter(job_type=job_type)
            query_result = [i for i in jobs if re.search(job_title, i.title)]
        elif job_title != '' and job_type == '' and location != '':
            jobs = models.Job.objects.filter(location=location)
            query_result = [i for i in jobs if re.search(job_title, i.title)]
        else:
            query_result = []
    context = {'query_result':query_result}
    return render(request, 'recruitment/job-query.html', context=context)

def about(request):
    return render(request, 'recruitment/about.html')

def job_detail(request, slug):
    job = get_object_or_404(models.Job, slug=str(slug))

    context = {'job':job}
    return render(request, 'recruitment/job-detail.html', context=context)

def detailed_application(request, slug):
    if request.method == 'POST':
        form = forms.DetailedApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.job_title = str(slug)
            post.save()
            return redirect('application-successful/')
    else:
        form = forms.DetailedApplicationForm()
    context = {'slug':str(slug), 'detailedApplicationForm':form}
    return render(request, 'recruitment/detailed-application.html', context=context)

def contact(request):
    return render(request, 'recruitment/contact.html')

def blog(request):
    return render(request, 'recruitment/blog.html')

def job_added(request):
    return render(request, 'recruitment/job-added.html')

def application_successful(request, *args):
    return render(request, 'recruitment/application-successful.html')

def post_job(request):
    if request.method == 'POST':
        form = forms.JobCreationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('job-added-successfully/')
    else:
        form = forms.JobCreationForm()
    context = {'jobCreationForm':form}
    return render(request, 'recruitment/new-post.html', context=context)

def want_job(request):
    return render(request, 'recruitment/job-post.html')