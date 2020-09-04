"""
RecruitmentFirm URL Configuration

"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from Recruitment import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recruitment/', include('Recruitment.urls', namespace='recruitment')),
    path('', views.index, name='homePage'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
