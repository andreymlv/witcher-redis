# views.py: это файл, в котором мы обрабатываем цикл запроса / ответа нашего веб-приложения.

from django.shortcuts import render
from .models import Person
import json

# Create your views here.


def home(request):

    with open('tree/templates/tree/data.json') as file:
        data = json.load(file)

    for states_data in data:
        if (states_data['id'] < 4):
            state, created = Person.objects.update_or_create(
                identifier=states_data['id'], 
                name=states_data['name'], 
                image=states_data['image']
            )
    
    for rulers_data in data:
        if (rulers_data.get('parent') == 1):
            ruler, created = Person.objects.update_or_create(
                identifier=rulers_data['id'], 
                name=rulers_data['name'],
                post= rulers_data['post'],
                image=rulers_data['image'],
                parent_id=rulers_data['parent'],
                chief=Person.objects.get(identifier=1)
            )
 
    states = Person.objects.filter(parent_id=None).order_by('identifier')
    rulers = Person.objects.filter(parent_id=1).order_by('identifier')

    states_list = list()
    rulers_list = list()

    for state in states:
        person_info = {
            "id": state.identifier,
            "name": state.name,
            "image": state.image
        }
        states_list.append(person_info)
    
    for ruler in rulers:
        person_info = {
            "name": ruler.name,
            "image": ruler.image
        }
        rulers_list.append(person_info)

    context = {
        'states_info': states_list,
        'rulers_info': rulers_list
    }

    return render(request, 'tree/index.html', context)
