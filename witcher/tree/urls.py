# urls.py: этот файл отвечает за отображение маршрутов и путей в нашем приложении.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('persons', views.persons_page, name='persons_page')
]
