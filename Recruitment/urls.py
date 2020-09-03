from django.urls import path
from . import views
app_name = 'recruitment'

urlpatterns = [
    path('about-us/', views.about, name='about-us'),
    path('contact-us/', views.contact, name='contact-us'),
    path('see-blog-posts/', views.blog, name='blog'),
    path('post-a-new-job/', views.post_job, name='post-job'),
    path('apply-for-a-job/', views.want_job, name='want-job'),
]