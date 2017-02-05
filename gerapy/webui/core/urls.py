from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^clients/$', views.clients, name='clients'),
    url(r'^client/(\d+)/$', views.client, name='client'),
    url(r'^spiders/$', views.spiders, name='spiders'),
    url(r'^spider/(\d+)/$', views.spider, name='spider'),
    url(r'^spider/(\d+)/edit/$', views.spider_edit, name='spider_edit'),
]
