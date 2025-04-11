# urls.py
"""
Файл маршрутов для Django проекта. Здесь задаются все URL-адреса для приложения.
"""

from django.urls import path
from . import views

# Указываем маршруты для всех страниц
urlpatterns = [
    path('', views.index, name='index'),  # Главная страница викторины
    path('check/', views.check_answer, name='check_answer'),  # Страница проверки ответа
    path('add/', views.add_pair, name='add_pair'),  # Страница добавления новой пары
    path('history/', views.history, name='history'),  # Страница истории ответов
    path('reset_history/', views.reset_history, name='reset_history'),  # Страница для сброса
]
