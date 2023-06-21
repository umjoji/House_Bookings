from django_filters import FilterSet
from .models import House

class HouseFilter(FilterSet):
    class Meta:
        model = House
        fields = ['name',
                  'city_id',
                  'state_id',
                  'amenities',
                  'number_of_beds',
                  'number_of_bath',
                  'pet_allowed',
                  'smoking_allowed',
        ]