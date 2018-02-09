import django.contrib.auth.urls
from django.urls import path,include
from django.contrib.auth import views as auth_views

app_name = 'Accounts'

# urlpatterns = [
#     #path('entrar', auth_views.LoginView.as_view()),
#     path(r'^entrar/$', auth_views.LoginView.as_view(template_name='accounts/login.html'),name='accounts'),
#
#     #path('entrar/',login.as_view(template_name="accounts/login.html", name="login")),
# ]


#Add Django site authentication urls (for login, logout, password management)
urlpatterns = [
    path('entrar/', include('django.contrib.auth.urls'),name='login'),
]
