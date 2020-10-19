# from django.contrib import admin
from django.urls import path
from vacancies.views import VacancyView, VacancyListView, SpecialtyCardView

urlpatterns = [
    path('', VacancyListView.as_view(), name='vacancies'),
    path('cat/<slug:category>/', SpecialtyCardView.as_view(), name='category'),
    path('<int:vacancy_id>/', VacancyView.as_view(), name='vacancy')
]
