from django.http import JsonResponse
from django.shortcuts import render
from localflavor.br.br_states import STATE_CHOICES
from .forms import StateForm
from .models import Person, City, District

def index(request):
    context = {}
    person_list = Person.objects.all()
    context['persons'] = person_list
    context['cities'] = City.objects.all()
    context['districts'] = District.objects.all()
    return render(request, 'prueba/listado.html', context)


def districts_choices_ajax(request):
    city = request.GET.get('city')
    districts = District.objects.filter(city=city)
    context = {'districts': districts}
    return render(request, 'includes/_districts_choices.html', context)


"""
def index(request):
    context = {}
    person_list = Person.objects.all()
    context['person_list'] = person_list
    return render(request, 'index.html', context)


def person_json(request):
    persons = Person.objects.all()
    data = [person.to_dict_json() for person in persons]
    response = {'data': data}
    return JsonResponse(response)


def filter_list(request):
    context = {}
    cities = City.objects.all()
    districts = District.objects.all()
    # context['states'] = STATE_CHOICES
    context['states'] = (
        ('MG', 'Minas Gerais'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('SP', 'São Paulo'),
    )
    context['cities'] = cities
    context['districts'] = districts
    return render(request, 'filter_list.html', context)


def filter_dropdown(request):
    context = {}
    context['form'] = StateForm
    # Filtro
    q = request.GET.get('district')
    if q:
        q = q.replace('.', '')
        persons = Person.objects.filter(district=str(q))
        context['persons'] = persons
    return render(request, 'filter_dropdown.html', context)


def filter_dropdown2(request):
    context = {}
    state = request.GET.get('state')
    city = request.GET.get('city')
    context['form'] = StateForm(state, city)
    # Filtro
    q = request.GET.get('district')
    if q:
        q = q.replace('.', '')
        persons = Person.objects.filter(district=str(q))
        context['persons'] = persons
    return render(request, 'filter_dropdown2.html', context)


def cities_ajax(request):
    uf = request.GET.get('uf')
    cities = City.objects.filter(uf=uf)
    context = {'cities': cities}
    return render(request, 'includes/_cities.html', context)


def cities_choices_ajax(request):
    uf = request.GET.get('uf')
    cities = City.objects.filter(uf=uf)
    context = {'cities': cities}
    return render(request, 'includes/_cities_choices.html', context)


def districts_ajax(request):
    city = request.GET.get('city')
    districts = District.objects.filter(city=city)
    context = {'districts': districts}
    return render(request, 'includes/_districts.html', context)


def districts_choices_ajax(request):
    city = request.GET.get('city')
    districts = District.objects.filter(city=city)
    context = {'districts': districts}
    return render(request, 'includes/_districts_choices.html', context)
"""