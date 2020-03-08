# views.py: это файл, в котором мы обрабатываем цикл запроса / ответа нашего веб-приложения.

from django.shortcuts import render
import requests

# Create your views here.
def home(request):

    url = 'https://raw.githubusercontent.com/poshekhon/witcher-redis/master/witcher/tree/data/input.js'
    data = requests.get(url).json()

    print(data)

    return render(request, 'tree/index.html')
