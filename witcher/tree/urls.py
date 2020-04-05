# urls.py: этот файл отвечает за отображение маршрутов и путей в нашем приложении.

from django.urls import path

from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('persons/', views.persons_page, name='persons_page'),
    path('persons/<int:pk>/', views.person_detail, name='person_detail'),
    path('update/', views.delete_and_update_persons, name='delete_and_update_persons')
]
