from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, F, Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Vacancy, Company, Specialty, Application, Resume
from .forms import CreateCompanyForm, VacancyForm, ApplicationForm, MyResumeForm


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
        context = {'specialty': specialty,
                   'vacancies': specialty_vacancies,
                   }
        return render(request, "vacancies/specialty_vacancies.html", context=context)


class CompanyCardView(View):
    def get(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        company_vacancies = Vacancy.objects.filter(company=company)

        context = {'company': company,
                   'vacancies': company_vacancies,
                   }
        return render(request, "vacancies/company_vacancies.html", context=context)


class VacancyView(View):
    def get(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
        form = ApplicationForm()
        context = {'vacancy': vacancy, 'form': form}
        return render(request, "vacancies/vacancy.html", context=context)

    def post(self, request, vacancy_id):
        application_form = ApplicationForm(request.POST)
        if application_form.is_valid():
            application = application_form.save(commit=False)
            application.user = request.user
            application.vacancy = Vacancy.objects.get(pk=vacancy_id)
            application.save()
            return redirect("sent", vacancy_id=vacancy_id)
        context = {"form": application_form}
        messages.error(request, "Ошибка валидации")
        return render(request, "vacancies/vacancy.html", context=context)


class MyCompanyStartView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "vacancies/company-create.html")


class MyCompanyCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = CreateCompanyForm()
        context = {'form': form}
        return render(request, "vacancies/company-edit.html", context=context)

    def post(self, request):
        company_form = CreateCompanyForm(request.POST, request.FILES)
        if company_form.is_valid():
            company = company_form.save(commit=False)
            company.owner = request.user
            company.save()
            messages.success(request, "Компания создана успешно")
            return redirect("edit_company")
        context = {"form": company_form}
        messages.error(request, "Ошибка валидации")
        return render(request, "vacancies/company-edit.html", context=context)


class MyCompanyEdit(LoginRequiredMixin, View):
    def get(self, request):
        try:
            company = request.user.company
        except Company.DoesNotExist:
            return redirect("my_company")
        bound_form = CreateCompanyForm(instance=company)
        context = {'form': bound_form, 'company': company}
        return render(request, "vacancies/company-edit.html", context=context)

    def post(self, request):
        company = request.user.company
        company_form = CreateCompanyForm(request.POST, request.FILES, instance=company)
        if company_form.is_valid():
            company_form.save()
            messages.success(request, "Информация обновлена успешно")
            return redirect("edit_company")
        context = {"form": company_form, 'company': company}
        messages.error(request, "Ошибка валидации")
        return render(request, "vacancies/company-edit.html", context=context)


class MyVacancies(LoginRequiredMixin, View):
    def get(self, request):
        try:
            vacancies = Vacancy.objects.filter(company=request.user.company)
        except Company.DoesNotExist:
            messages.error(request, "Создайте компанию, чтоб добавлять вакансии")
            vacancies = []
            company_exists = False
        else:
            company_exists = True
        if not vacancies:
            messages.info(request, "У вас пока нет вакансий, но вы можете создать первую!")
        context = {'vacancies': vacancies, 'company_exists': company_exists}
        return render(request, "vacancies/vacancy-list.html", context=context)


class MyVacancyEdit(LoginRequiredMixin, View):
    def get(self, request, vacancy_id):
        vacancy = Vacancy.objects.get(pk=vacancy_id)
        applications = Application.objects.filter(vacancy=vacancy)
        bound_form = VacancyForm(instance=vacancy)
        context = {'form': bound_form, 'vacancy': vacancy,
                   "show_applications": True, 'applications': applications}
        return render(request, "vacancies/vacancy-edit.html", context=context)

    def post(self, request, vacancy_id):
        vacancy = Vacancy.objects.get(pk=vacancy_id)
        applications = Application.objects.filter(vacancy=vacancy)
        vacancy_form = VacancyForm(request.POST, instance=vacancy)
        if vacancy_form.is_valid():
            vacancy_form.save()
            messages.success(request, "Информация обновлена успешно")
            return redirect("my_vacancies")
        context = {"form": vacancy_form, 'vacancy': vacancy,
                   'show_applications': True, 'applications': applications}
        messages.error(request, "Ошибка валидации")
        return render(request, "vacancies/vacancy-edit.html", context=context)


class MyVacancyCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = VacancyForm()
        context = {'form': form, "show_applications": False}
        return render(request, "vacancies/vacancy-edit.html", context=context)

    def post(self, request):
        vacancy_form = VacancyForm(request.POST)
        if vacancy_form.is_valid():
            unsaved_form = vacancy_form.save(commit=False)
            unsaved_form.company = request.user.company
            vacancy_form.save()
            messages.success(request, "Ваканасия успешно создана")
            return redirect("my_vacancies")
        context = {"form": vacancy_form, "show_applications": False}
        messages.error(request, "Ошибка валидации")
        return render(request, "vacancies/vacancy-edit.html", context=context)


@login_required
def sent(request, vacancy_id):
    vacancy = Vacancy.objects.get(pk=vacancy_id)
    return render(request, 'vacancies/sent.html', {'vacancy': vacancy})


class SearchView(View):
    def get(self, request):
        search_query = request.GET.get('s')
        if search_query:
            vacancies = Vacancy.objects.filter(Q(title__icontains=search_query) |
                                               Q(skills__icontains=search_query) |
                                               Q(description__icontains=search_query))
        else:
            vacancies = Vacancy.objects.all()

        context = {'vacancies': vacancies}
        return render(request, "vacancies/search.html", context=context)


class MyResumeStartView(LoginRequiredMixin, View):
    def get(self, request):
        context = {}
        return render(request, "vacancies/resume-create.html", context=context)


class MyResumeCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = MyResumeForm()
        context = {'form': form}
        return render(request, "vacancies/resume-edit.html", context=context)

    def post(self, request):
        resume_form = MyResumeForm(request.POST)
        if resume_form.is_valid():
            resume = resume_form.save(commit=False)
            resume.user = request.user
            resume.save()
            messages.success(request, "Резюме создано")
            return redirect("edit_resume")
        context = {"form": resume_form}
        messages.error(request, "Ошибка валидации")
        return render(request, "vacancies/resume-edit.html", context=context)


class MyResumeEdit(LoginRequiredMixin, View):
    def get(self, request):
        try:
            resume = request.user.resume
        except Resume.DoesNotExist:
            return redirect("create_resume")
        resume_form = MyResumeForm(instance=resume)
        context = {'form': resume_form}
        return render(request, "vacancies/resume-edit.html", context=context)

    def post(self, request):
        resume = request.user.resume
        resume_form = MyResumeForm(request.POST, instance=resume)
        if resume_form.is_valid():
            resume = resume_form.save(commit=False)
            resume.user = request.user
            resume.save()
            messages.success(request, "Информация обновлена успешно")
            return redirect('edit_resume')
        context = {"form": resume_form, 'resume': resume}
        messages.error(request, "Ошибка валидации")
        return render(request, "vacancies/resume-edit.html", context=context)


def custom_404_handler(request, exception):
    return render(request, 'error_404.html')


def custom_500_handler(request):
    return render(request, 'error_500.html')
