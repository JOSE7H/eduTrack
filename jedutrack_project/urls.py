"""
URL configuration for jedutrack_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Dashboard import views
from Dashboard.views import dashboard

urlpatterns = [
    # Admin URL


    path('', views.dashboard, name='dashboard'),
    path('parent-dashboard', views.parent_dashboard, name='parent_dashboard'),
    path('teacher-dashboard', views.teacher_dashboard, name='teacher_dashboard'),


    path('admin/', admin.site.urls, name='admin'),


    # Authentication URLs

   ]