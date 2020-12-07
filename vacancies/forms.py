from django import forms
from django.core.exceptions import ValidationError

from vacancies.models import Company, Vacancy, Application, Resume


class CreateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'city', 'logo', 'description', 'employee_count', ]
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'city': forms.TextInput(attrs={"class": "form-control"}),
            'employee_count': forms.TextInput(attrs={"class": "form-control"}),
            'description': forms.Textarea(attrs={"class": "form-control",
                                                 "rows": 5,
                                                 "style": "color:#00000"}),
            'logo': forms.FileInput(attrs={"class": "custom-file-input"})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name[0].isupper():
            raise ValidationError("Имя компании должно начинаться с большой буквы")
        return name

    def clean_city(self):
        city = self.cleaned_data['city']
        if not city[0].isupper():
            raise ValidationError("Город должен начинаться с большой буквы")
        return city


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'salary_min', 'salary_max', 'skills', 'description', 'specialty']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'salary_min': forms.TextInput(attrs={"class": "form-control"}),
            'salary_max': forms.TextInput(attrs={"class": "form-control"}),
            'skills': forms.Textarea(attrs={"class": "form-control",
                                            "rows": 3,
                                            "style": "color: #000;"}),
            'description': forms.Textarea(attrs={"class": "form-control",
                                                 "rows": 13,
                                                 "style": "color: #000;"}),
            'specialty': forms.Select(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title[0].isupper():
            raise ValidationError("Название вакансии должно начинаться с большой буквы")
        return title

    def clean_salary_max(self):
        max_sal, min_sal = self.cleaned_data.get('salary_max', 0), self.cleaned_data.get('salary_min', 0)
        if max_sal < min_sal:
            raise ValidationError("Верхняя граница зарплаты должна быть не меньше нижней")
        return max_sal


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter']
        widgets = {
            'written_username': forms.TextInput(attrs={"class": "form-control"}),
            'written_phone': forms.TextInput(attrs={"class": "form-control",
                                                    "type": "tel"}),
            'written_cover_letter': forms.Textarea(attrs={"class": "form-control",
                                                          "rows": 8}),
        }


class MyResumeForm(forms.ModelForm):
    class Meta:
        GRADE_CHOICE = [
            ('lead', 'Лид'),
            ('senior', 'Синьор'),
            ('middle', 'Мидл'),
            ('junior', 'Джуниор'),
            ('trainee', 'Стажер')
        ]
        STATUS_CHOICE = [
            ('in_the_search', 'Ищу работу'),
            ('consider_offers', 'Рассматриваю предложения'),
            ('not_in_the_search', 'Не ищу работу')
        ]
        SPECIALTY_CHOICE = [
            ('frontend', 'Фронтенд-разработчик'),
            ('backend', 'Бекенд-Разработчик'),
            ('fullstack', 'Фулстек-разработчик'),

        ]
        model = Resume
        fields = ['name', 'surname', 'status', 'grade',
                  'experience', 'salary', 'specialty', 'education', 'portfolio', ]
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'surname': forms.TextInput(attrs={"class": "form-control"}),
            'status': forms.Select(choices=STATUS_CHOICE,
                                   attrs={"class": "form-control"}),
            'grade': forms.Select(choices=GRADE_CHOICE,
                                  attrs={"class": "form-control"}),
            'experience': forms.Textarea(attrs={"class": "form-control",
                                                "style": "color:#000",
                                                "rows": 4
                                                }),
            'salary': forms.TextInput(attrs={"class": "form-control"}),
            'specialty': forms.Select(choices=SPECIALTY_CHOICE,
                                      attrs={"class": "form-control"}),
            'education': forms.Textarea(attrs={"class": "form-control",
                                               "style": "color:#000",
                                               "rows": 4
                                               }),
            'portfolio': forms.URLInput(attrs={"placeholder": "http://anylink.github.io",
                                                "style": "color:#000",
                                                "class": "form-control"}),
        }
