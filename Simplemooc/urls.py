from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from Simplemooc.core import views
admin.autodiscover()

urlpatterns = [
    #path(r'', views.home, name='home'),
    #path(r'contato/',views.contacts, name='contato'),
    path(r'', include('Simplemooc.core.urls',namespace='Simplemooc')),
    path(r'cursos/',include('Simplemooc.courses.urls',namespace='Courses')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
