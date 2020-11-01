from django import template

register = template.Library()


@register.inclusion_tag('vacancies/inc/_back.html')
def back_button(request):
    return {'back': request.META.get("HTTP_REFERER")}
