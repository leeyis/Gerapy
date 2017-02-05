from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^clients/$', views.clients, name='clients'),
    url(r'^client/(\d+)/$', views.client, name='client'),
    url(r'^client/(\d+)/edit/$', views.client_edit, name='client_edit'),
]