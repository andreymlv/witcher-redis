# views.py: это файл, в котором мы обрабатываем цикл запроса / ответа нашего веб-приложения.

from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from .models import Person
import json
from django.db.models import Count


def start(request):
    """
    Рендерит начальную страницу, где находятся штаты (государства)
    """

    states = Person.objects.order_by('id').filter(parent=None).values()
    states_list = list()
    subordinates = Person.objects.order_by('id').filter(parent__lte=len(states)).values()
    subordinates_list = list()

    for state in states:
        state_info = dict(state)

        for subordinate in subordinates:
            subordinates_list.append(dict(subordinate))
        
        states_list.append(state_info)

    context = {
        'state_info' : states_list,
        'subordinate_info': subordinates_list
    }

    return render(request, 'tree/home.html', context)

def persons_page(request):
    """
    Рендерит страницу со всеми персонажами, для удобного отслеживания, кто есть в базе данных.
    """

    persons = Person.objects.order_by('id').values()
    persons_list = list()

    for person in persons:
        persons_list.append(dict(person))


    context = {
        'person_info': persons_list
    }

    return render(request, 'tree/persons.html', context)


def person_detail(request, pk):
    """
    Берёт из базы данных персонажа, и возвращает информацию о нём.
    """

    person = get_object_or_404(Person, id=pk)

    if (person.number_subordinates_hr != 0):
        subordinates = list(Person.objects.order_by('id').filter(parent=person.id).values())

        context = {
            'person': person,
            'subordinates': subordinates
        }
    else:
        context = {
            'person': person
        }

    return render(request, 'tree/person_detail.html', context)


def delete_and_update_persons(request):
    """
    Удаляет все данные о персонажах, и загружает (обновляет) новые данные из файла tree/data.json
    """
    Person.objects.all().delete()

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


    return redirect('/')
