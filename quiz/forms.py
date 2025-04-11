"""
Формы
""" 

from django import forms

class QuizForm(forms.Form):
    """
    Форма для проведения викторины.
    Скрытое поле 'country' хранит название страны.
    Поле 'answer' предназначено для ввода пользователем предполагаемой столицы.
    """
    country = forms.CharField(widget=forms.HiddenInput())
    answer = forms.CharField(label='Столица', max_length=100, required=True)

class AddPairForm(forms.Form):
    """
    Форма для добавления новой пары страна-столица.
    Поля 'country' и 'capital' предназначены для ввода названия страны и её столицы соответственно.
    """
    country = forms.CharField(label='Страна', max_length=100, required=True)
    capital = forms.CharField(label='Столица', max_length=100, required=True)
