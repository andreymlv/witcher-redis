# views.py: это файл, в котором мы обрабатываем цикл запроса / ответа нашего веб-приложения.

from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Hello, World!')
