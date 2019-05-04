from django.http import HttpResponse
from django.shortcuts import render

from .models import City, Country, State


def filter(request):
    context = {}
    context['country'] = Country.objects.all()
    context['state'] = State.objects.none
    context['city'] = City.objects.none
    return render(request, 'filter.html', context)


def filter_result(request):
    data = Country.objects.all()
    context = {'dataset': data}
    return render(request, 'includes/table_result.html', context)


def country_choices_ajax(request):
    data = Country.objects.all()
    context = {'countries': data}
    return render(request, 'includes/country_choices.html', context)


def state_choices_ajax(request):
    countryId = request.GET['uf']
    countryOb = Country.objects.get(id=countryId)
    data = State.objects.filter(country=countryOb)
    context = {'states': data}
    return render(request, 'includes/state_choices.html', context)


def city_choices_ajax(request):
    stateId = request.GET['uf']
    stateOb = State.objects.get(id=stateId)
    data = City.objects.filter(state=stateOb)
    context = {'cities': data}
    return render(request, 'includes/city_choices.html', context)
