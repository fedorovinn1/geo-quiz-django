"""
Пользовательские теги и фильтры для шаблонов.
"""

from django import template

# Регистрируем фильтр для шаблонов
register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    """
    Фильтр для добавления CSS класса к полям формы.

    Аргументы:
        field (django.forms.Field): Поле формы.
        css_class (str): CSS класс для добавления к полю.

    Возвращает:
        django.forms.Widget: Поле формы с добавленным CSS классом.
    """
    return field.as_widget(attrs={"class": css_class})
