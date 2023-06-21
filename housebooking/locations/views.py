from django.shortcuts import render
from.models import Country, State, City
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

class CountryCreate(CreateView):
    model = Country

class CountryUpdate(UpdateView):
    model = Country

class CountryDelete(DeleteView):
    model = Country

class StateCreate(CreateView):
    model = State

class StateUpdate(UpdateView):
    model = State

class StateDelete(DeleteView):
    model = State

class CityCreate(CreateView):
    model = City

class CityUpdate(UpdateView):
    model = City

class CityDelete(DeleteView):
    model = City