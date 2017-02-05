from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^clients/$', views.clients, name='clients'),
    url(r'^client/(\d+)/$', views.client, name='client'),
    url(r'^client/create/$', views.client_create, name='client_create'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^project/(\d+)/$', views.project, name='project'),
    url(r'^project/(\d+)/edit/$', views.project_edit, name='project_edit'),
    url(r'^project/create/$', views.project_create, name='project_create'),
]
