"""southflalerts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Insertvalue),
    path('unsubscribe/', views.Deletevalue),
    path('contact/', views.ContactUs),
    path('changelog/', TemplateView.as_view(template_name='Changelog.html')),
    path('faq/', TemplateView.as_view(template_name='FAQ.html')),
]

handler404 = 'southflalerts.views.My404'
handler500 = 'southflalerts.views.My500'