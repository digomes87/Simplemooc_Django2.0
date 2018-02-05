from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'Simplemooc'
urlpatterns = [
    path(r'',views.home, name='home'),
    path(r'contato/',views.contacts, name='contato'),
]
