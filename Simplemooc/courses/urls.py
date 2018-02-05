from django.contrib import admin
from django.urls import path, include, re_path

from . import views

app_name = 'Courses'
urlpatterns = [
    path(r'',views.index, name='index'),
    #re_path(r'^(?P<pk>\d+)/$', views.details, name='details')
    re_path(r'^(?P<slug>[\w_-]+)/$', views.details, name='details')
]
