# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.VacancyListView.as_view(), name='vacancies'),
    path('cat/<slug:category>/', views.SpecialtyCardView.as_view(), name='category'),
    path('<int:vacancy_id>/', views.VacancyView.as_view(), name='vacancy'),
    path('<int:vacancy_id>/sent/', views.sent, name='sent'),
]
