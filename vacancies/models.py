from django.utils.timezone import now
from django.db import models
from django.urls import reverse


class Vacancy(models.Model):
    title = models.CharField(max_length=32)
    specialty = models.ForeignKey('Specialty', on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(null=True, max_length=100)
    description = models.TextField(null=True)
    salary_min = models.PositiveIntegerField()
    salary_max = models.PositiveIntegerField()
    published_at = models.DateField(default=now)

    def get_absolute_url(self):
        return reverse('vacancy', kwargs={'vacancy_id': self.pk})

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(max_length=32, unique=True)
    city = models.CharField(max_length=32)
    # logo = models.ImageField()
    description = models.TextField()
    employee_count = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse('company', kwargs={'company_id': self.pk})

    def __str__(self):
        return self.name


class Specialty(models.Model):
    code = models.SlugField(max_length=32, unique=True)
    title = models.CharField(max_length=32)

    # picture = models.ImageField()

    def get_absolute_url(self):
        return reverse('category', kwargs={'category': self.code})

    def __str__(self):
        return self.title
