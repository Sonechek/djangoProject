"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from hdver2 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('form/', views.form, name='form'),
    path('form/create/', views.create),
    path('tickets', views.ticket, name='tickets'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('close/<int:id>/', views.close_ticket, name='close'),
    path('reports/', views.reports, name='reports'),
    path('accounts/', include('django.contrib.auth.urls'), name='accounts'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
