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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from vacancies import views

handler404 = views.custom_404_handler
handler500 = views.custom_500_handler

urlpatterns = [
    path('', views.MainPageView.as_view(), name='home'),
    path('', include('authentication.urls')),
    path('companies/<int:company_id>/', views.CompanyCardView.as_view(), name='company'),
    path('vacancies/', include('vacancies.urls')),
    path('search/', views.SearchView.as_view(), name='search'),
    path('mycompany/', views.MyCompanyStartView.as_view(), name='my_company'),
    path('mycompany/send/', views.MyCompanyCreateView.as_view(), name='create_company'),
    path('mycompany/edit/', views.MyCompanyEdit.as_view(), name='edit_company'),
    path('mycompany/vacancies/', views.MyVacancies.as_view(), name='my_vacancies'),
    path('mycompany/vacancies/create/', views.MyVacancyCreate.as_view(), name='create_vacancy'),
    path('mycompany/vacancies/<int:vacancy_id>/', views.MyVacancyEdit.as_view(), name='edit_vacancy'),
    path('myresume/', views.MyResumeStartView.as_view(), name='my_resume'),
    path('myresume/create/', views.MyResumeCreate.as_view(), name='create_resume'),
    path('myresume/edit/', views.MyResumeEdit.as_view(), name='edit_resume'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
