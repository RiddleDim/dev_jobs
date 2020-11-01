from django.contrib.auth import get_user_model
from django.utils.timezone import now
from django.db import models
from django.urls import reverse
from conf.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR


class Vacancy(models.Model):
    title = models.CharField(max_length=32)
    specialty = models.ForeignKey('Specialty', on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(null=True, blank=True, max_length=100)
    description = models.TextField(null=True, blank=True)
    salary_min = models.PositiveIntegerField()
    salary_max = models.PositiveIntegerField()
    published_at = models.DateField(default=now)

    def get_absolute_url(self):
        return reverse('vacancy', kwargs={'vacancy_id': self.pk})

    def get_update_url(self):
        return reverse('edit_vacancy', kwargs={'vacancy_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"


class Company(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    logo = models.ImageField(upload_to=f'{MEDIA_COMPANY_IMAGE_DIR}', null=True, blank=True)
    description = models.TextField()
    employee_count = models.PositiveIntegerField()
    owner = models.OneToOneField(get_user_model(), on_delete=models.PROTECT, related_name='company')

    def get_absolute_url(self):
        return reverse('company', kwargs={'company_id': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class Specialty(models.Model):
    code = models.SlugField(max_length=32, unique=True, verbose_name='Код')
    title = models.CharField(max_length=32, verbose_name='Название')
    picture = models.ImageField(upload_to=f'{MEDIA_SPECIALITY_IMAGE_DIR}', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category': self.code})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"
        ordering = ['title']


class Application(models.Model):
    written_username = models.CharField(max_length=32)
    written_phone = models.CharField(max_length=13)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name="applications")

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"


class Resume(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.PROTECT,
                                related_name='resume')
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    status = models.CharField(max_length=32)
    salary = models.PositiveIntegerField()
    specialty = models.CharField(max_length=32)
    education = models.CharField(max_length=64)
    grade = models.CharField(max_length=64)
    experience = models.TextField()
    portfolio = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"
