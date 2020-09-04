from django.urls import path
from . import views
app_name = 'recruitment'

urlpatterns = [
    path('about-us/', views.about, name='about-us'),
    path('contact-us/', views.contact, name='contact-us'),
    path('see-blog-posts/', views.blog, name='blog'),
    path('post-a-new-job/', views.post_job, name='post-job'),
    path('apply-for-a-job/', views.want_job, name='want-job'),
    path('apply-for-a-job/see-job-details/<str:slug>', views.job_detail, name='job-details'),
    path('apply-for-a-job/see-job-details/apply-now/<str:slug>', views.detailed_application, name='detailed-application'),
    path('apply-for-a-job/see-job-details/apply-now/application-successful/',
         views.application_successful, name='application-successful'),
    path('post-a-new-job/job-added-successfully/', views.job_added, name='job-added'),
    path('jobs/query-results/', views.job_query, name='job-query'),
]