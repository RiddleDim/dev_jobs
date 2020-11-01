from django.contrib import admin

from vacancies.models import Specialty


class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('code', 'title')
    list_display_links = ('title',)
    search_fields = ('code', 'title')


admin.site.register(Specialty, SpecialtyAdmin)
