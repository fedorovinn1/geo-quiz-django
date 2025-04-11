"""
Файл маршрутов для Django проекта. Здесь задаются все URL-адреса для приложения.
"""

from django.urls import path, include

urlpatterns = [
    path('', include('quiz.urls')),
]
