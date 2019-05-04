from django.urls import path
from . import views

app_name = 'filterform'

urlpatterns = [
    path('', views.filter, name='filter'),
    path('country/choices/ajax/', views.country_choices_ajax, name='country_choices_ajax'),
    path('state/choices/ajax/', views.state_choices_ajax, name='state_choices_ajax'),
    path('city/choices/ajax/', views.city_choices_ajax, name='city_choices_ajax'),
    path('filter_result/<int:uf>/', views.filter_result, name='filter_result'),
]
