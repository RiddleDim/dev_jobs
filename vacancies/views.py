from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Vacancy, Company, Specialty


class MainPageView(View):
    def get(self, request):
        specialties = Specialty.objects.all().annotate(vac_count=Count('vacancies'))
        companies = Company.objects.all().annotate(vac_count=Count('vacancies'))
        fast_categories = ['Python', 'Flask', 'Django', 'DevOps', 'ML']
        context = {'specialties': specialties,
                   'fast_categories': fast_categories,
                   'companies': companies}
        return render(request, "vacancies/index.html", context=context)


class VacancyListView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        context = {'vacancies': vacancies}
        return render(request, "vacancies/vacancies.html", context=context)


class SpecialtyCardView(View):
    def get(self, request, category):
        specialty = get_object_or_404(Specialty, code=category)
        specialty_vacancies = Vacancy.objects.filter(specialty=specialty)
        context = {'criteria': specialty,
                   'vacancies': specialty_vacancies,
                   'title': 'специальностям'}
        return render(request, "vacancies/filtered_vacancies.html", context=context)


class CompanyCardView(View):
    def get(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        company_vacancies = Vacancy.objects.filter(company=company)
        context = {'criteria': company,
                   'vacancies': company_vacancies,
                   'title': 'компаниям'}
        return render(request, "vacancies/filtered_vacancies.html", context=context)


class VacancyView(View):
    def get(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
        context = {'vacancy': vacancy}
        return render(request, "vacancies/vacancy.html", context=context)


def custom_404_handler(request, exception):
    return render(request, 'error_404.html')


def custom_500_handler(request):
    return render(request, 'error_500.html')
