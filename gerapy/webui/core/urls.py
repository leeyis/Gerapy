from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^clients/$', views.clients, name='clients'),
    url(r'^client/edit/(\d+)/$', views.client_edit, name='client_edit'),
    url(r'^client/schedule/(\d+)/$', views.client_schedule, name='client_schedule'),
    url(r'^client/create/$', views.client_create, name='client_create'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^project/deploy/(\d+)/(\d+)?$', views.project_deploy, name='project_deploy'),
    url(r'^project/edit/(\d+)/$', views.project_edit, name='project_edit'),
    url(r'^project/pack/(\d+)/$', views.project_pack, name='project_pack'),
    url(r'^project/create/$', views.project_create, name='project_create'),
    url(r'^project/jobs/(\d+)/$', views.project_jobs, name='project_jobs'),
    url(r'^version/delete/(\d+)/(\d+)/$', views.version_delete, name='version_delete'),
    url(r'^spider/schedule/(\d+)/$', views.spider_schedule, name='spider_schedule'),
    url(r'^job/cancel/(\d+)/$', views.job_cancel, name='job_cancel'),
    url(r'^job/log/(\d+)/$', views.job_log, name='job_log'),
]
