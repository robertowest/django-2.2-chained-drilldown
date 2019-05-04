from django.urls import path
from . import views as v

app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('districts/choices/ajax/', v.districts_choices_ajax, name='districts_choices_ajax'),
]

"""
urlpatterns = [
    path('', v.index, name='index'),
    path('person/json/', v.person_json, name='person_json'),
    path('filter_list/', v.filter_list, name='filter_list'),
    path('filter_dropdown/', v.filter_dropdown, name='filter_dropdown'),
    path('filter_dropdown2/', v.filter_dropdown2, name='filter_dropdown2'),
    path('cities/ajax/', v.cities_ajax, name='cities_ajax'),
    path('cities/choices/ajax/', v.cities_choices_ajax, name='cities_choices_ajax'),
    path('districts/ajax/', v.districts_ajax, name='districts_ajax'),
    path('districts/choices/ajax/', v.districts_choices_ajax, name='districts_choices_ajax'),
]
"""