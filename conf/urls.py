"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from vacancies.views import MainPageView, CompanyCardView, custom_404_handler, custom_500_handler

handler404 = custom_404_handler
handler500 = custom_500_handler

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('companies/<int:company_id>', CompanyCardView.as_view(), name='company'),
    path('vacancies/', include('vacancies.urls')),
    path('admin/', admin.site.urls)
]
