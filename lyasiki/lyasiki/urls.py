from django.contrib import admin
from django.urls import path, include
from lyasikservice import views
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lyasikservice/', include('lyasikservice.urls')),
    path('', views.home, name='home'),
]
