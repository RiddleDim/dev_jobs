import os
from datetime import datetime

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'
django.setup()

from vacancies.models import Company, Specialty, Vacancy
from vacancies.data import companies, specialties, jobs


def add_specialties(spec_info: dict):
    for spec in spec_info:
        Specialty.objects.create(code=spec['code'], title=spec['title'])


def add_vacancies(vacancies_info: dict):
    for vacancy in vacancies_info:
        specialty = Specialty.objects.get(code=vacancy['cat'])
        company = Company.objects.get(name=vacancy['company'])
        publish_date = datetime.strptime(vacancy['posted'], "%Y-%m-%d")
        Vacancy.objects.create(title=vacancy['title'],
                               specialty=specialty,
                               company=company,
                               salary_min=vacancy['salary_from'],
                               salary_max=vacancy['salary_to'],
                               description=vacancy['desc'],
                               published_at=publish_date)


def add_companies(companies_info: dict):
    for company in companies_info:
        Company.objects.create(name=company['title'],
                               city="Kyiv",
                               description="Good Company",
                               employee_count=20000)


if __name__ == '__main__':
    add_vacancies(jobs)
    add_companies(companies)
    add_specialties(specialties)
