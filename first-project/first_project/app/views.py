import os
from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time_date = datetime.now()
    current_time = current_time_date.time()
    current_time_format = current_time.strftime('%H: %M: %S')
    msg = f'Текущее время: {current_time_format}'
    return HttpResponse(msg)


def workdir_view(request):
    msg = f'Рабочая директория: {",".join(os.listdir())}'
    return HttpResponse(msg)
