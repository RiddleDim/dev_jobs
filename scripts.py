import os
from datetime import datetime

from conf.settings import MEDIA_SPECIALITY_IMAGE_DIR, MEDIA_COMPANY_IMAGE_DIR, MEDIA_URL
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'
django.setup()

from vacancies.models import Company, Specialty, Vacancy, Resume
from vacancies.data import companies, specialties, jobs
from django.contrib.auth.models import User


def add_specialties(spec_info: dict):
    for spec in spec_info:
        Specialty.objects.create(code=spec['code'],
                                 title=spec['title'],
                                 picture=os.path.join(
                                                      MEDIA_SPECIALITY_IMAGE_DIR,
                                                      'specty_backend.png')
                                 )


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
    for pk, company in enumerate(companies_info, 1):
        Company.objects.create(name=company['title'],
                               city="Kyiv",
                               description="Good Company",
                               employee_count=20000,
                               logo=os.path.join(
                                                 MEDIA_COMPANY_IMAGE_DIR,
                                                 'logo1.png'),
                               owner=User.objects.get(pk=pk)

                               )
def add_users(user_count):
    for i in range(user_count):
        User.objects.create_user(username="John" + str(i),
                                 password = '123')


if __name__ == '__main__':
    Company.objects.all().delete()
    Specialty.objects.all().delete()
    add_users(20)
    add_companies(companies)
    add_specialties(specialties)
    add_vacancies(jobs)


