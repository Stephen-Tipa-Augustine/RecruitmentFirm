from django.shortcuts import render, redirect
from . import forms, models

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

def about(request):
    return render(request, 'recruitment/about.html')

def contact(request):
    return render(request, 'recruitment/contact.html')

def blog(request):
    return render(request, 'recruitment/blog.html')

def post_job(request):
    if request.method == 'POST':
        form = forms.JobCreationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = forms.JobCreationForm()
    context = {'jobCreationForm':form}
    return render(request, 'recruitment/new-post.html', context=context)

def want_job(request):
    return render(request, 'recruitment/job-post.html')