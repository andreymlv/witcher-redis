# views.py: это файл, в котором мы обрабатываем цикл запроса / ответа нашего веб-приложения.

from django.shortcuts import render
from .models import Person
import json
from django.db.models import Count


def home(request):

    # Открываю файл data.json, форматирую его в простой массив Python
    with open('tree/templates/tree/data.json') as file:
        data = json.load(file)

    # Обновляю или создаю в базе данных нужных мне персонажей
    for state_data in data:
        # Количество подчиненных
        count_of_subordinates_inside = 0
        if not ('parent' in state_data.keys()):
            state, created = Person.objects.update_or_create(
                **state_data
            )
        for person_data in data:
            if (person_data.get('parent') == state_data.get('id')):
                count_of_subordinates_inside += 1
                person, created = Person.objects.update_or_create(
                    **person_data,
                    chief=Person.objects.get(id__exact=state_data.get('id'))
                )

        Person.objects.filter(id__exact=state_data.get('id')).update(number_subordinates_hr=count_of_subordinates_inside)



    # Сортирую по ID
    states = Person.objects.filter(parent=None).order_by('id')

    # Списки будут хранить в себе информацию объектов, которые потом будут передоваться в контекст
    states_list = list()

    for state in states:
        person_info = {
            "id": state.id,
            "name": state.name,
            "image": state.image
        }
        states_list.append(person_info)

    context = {
        'states_info': states_list
    }

    return render(request, 'tree/states.html', context)


def persons_page(request):

    persons = Person.objects.order_by('id').values()
    persons_list = list()

    for person in persons:
        person_info = dict(person)
        print(person_info)
        persons_list.append(person_info)


    context = {
        'person_info': persons_list
    }

    return render(request, 'tree/persons.html', context)
