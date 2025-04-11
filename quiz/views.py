"""
Представления для приложения викторины.

Этот модуль содержит функции, обрабатывающие запросы, связанные с викториной: отображение вопросов,
проверка ответов, добавление новых пар страна-столица и другие.
"""

import json
import random
from django.shortcuts import render, redirect
from .forms import QuizForm, AddPairForm

# Константы для файлов данных
PAIRS_FILE = 'data/pairs.json'
HISTORY_FILE = 'data/history.json'


def load_pairs():
    """
    Загружает список пар стран и столиц из файла.

    Возвращает:
        list: Список словарей с парами стран и столиц.
    """
    with open(PAIRS_FILE, encoding='utf-8') as file:
        return json.load(file)


def save_pairs(pairs):
    """
    Сохраняет обновленный список пар стран и столиц в файл.

    Аргументы:
        pairs (list): Список пар стран и столиц.
    """
    with open(PAIRS_FILE, 'w', encoding='utf-8') as file:
        json.dump(pairs, file, ensure_ascii=False, indent=2)


def load_history():
    """
    Загружает историю ответов пользователя из файла.
    """
    with open(HISTORY_FILE, encoding='utf-8') as file:
        return json.load(file)


def save_history(history):
    """
    Сохраняет историю ответов пользователя в файл.
    """
    with open(HISTORY_FILE, 'w', encoding='utf-8') as file:
        json.dump(history, file, ensure_ascii=False, indent=2)


def index(request):
    """
    Отображает страницу с вопросом викторины.
    Выбирает случайную пару страна-столица и отображает форму.
    """
    pairs = load_pairs()
    pair = random.choice(pairs)
    form = QuizForm(initial={'country': pair['country']})
    return render(request, 'quiz/index.html', {'form': form, 'country': pair['country']})


def check_answer(request):
    """Проверяет ответ пользователя и добавляет его в историю."""
    if request.method == 'POST':
        country = request.POST.get('country')
        user_answer = request.POST.get('answer').strip().lower()

        correct = False
        pairs = load_pairs()
        for pair in pairs:
            if pair['country'] == country and pair['capital'].lower() == user_answer:
                correct = True
                break

        history_data = load_history()  
        history_data.append({
            'country': country,
            'user_answer': user_answer,
            'correct': correct
        })
        save_history(history_data)  

        return render(request, 'quiz/result.html', {
            'correct': correct,
            'country': country,
            'user_answer': user_answer,
            'right_answer': next(
                (p['capital'] for p in pairs if p['country'] == country),
                'Неизвестно'
            )
        })

    return redirect('index')


def add_pair(request):
    """
    Позволяет администратору добавить новую пару страна-столица.
    Отображает форму для ввода новой пары и сохраняет её в файл.
    """
    if request.method == 'POST':
        form = AddPairForm(request.POST)
        if form.is_valid():
            new_pair = {
                'country': form.cleaned_data['country'],
                'capital': form.cleaned_data['capital']
            }
            pairs = load_pairs()
            pairs.append(new_pair)
            save_pairs(pairs)
            return redirect('index')
    else:
        form = AddPairForm()
    return render(request, 'quiz/add_pair.html', {'form': form})


def history(request):
    """
    Отображает страницу с историей ответов пользователя.
    Загружает и отображает историю всех предыдущих ответов.
    """
    history_data = load_history()
    return render(request, 'quiz/history.html', {'history': history_data})


def reset_history(_):
    """
    Очищает всю историю ответов пользователя.
    После сброса истории редиректит на страницу истории.
    """
    save_history([])  # Сохраняем пустую историю
    return redirect('history')
