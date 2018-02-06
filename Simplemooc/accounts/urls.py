from django.urls import path
from . import views

app_name = 'Accounts'
urlpatterns = [
    path(r'',views.accounts, name='accounts')
]
