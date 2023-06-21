from typing import Any
from django.db import models
import uuid
from landlords.models import LandLord
# import django_filters
from locations.models import State, City
from django.urls import reverse
from home.models import User

OPTIONS = (
    ('yes', 'YES'),
    ('no', 'NO'),
)

HOUSE_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'Occupied'),
        ('a', 'Available'),
        ('r', 'Reserved'),
)

def gen_pk_amenity():
    return f"AME-{uuid.uuid4().hex[:5].upper()}"

def gen_pk_house():
    return f"HOU-{uuid.uuid4().hex[:5].upper()}"

def gen_pk_image():
    return f"IMG-{uuid.uuid4().hex[:5].upper()}"


class Amenity(models.Model):
    amenity_id = models.CharField(primary_key=True, default=gen_pk_amenity, max_length=20, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class House(models.Model):
    house = models.CharField(primary_key=True, default=gen_pk_house, max_length=50, editable=False)
    landlord = models.ForeignKey(LandLord, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    amenities = models.ManyToManyField(Amenity, help_text="Add amenities")
    number_of_beds = models.PositiveIntegerField()
    number_of_bath = models.PositiveIntegerField()
    pet_allowed = models.CharField(max_length=10, choices=OPTIONS)
    smoking_allowed = models.CharField(max_length=10, choices=OPTIONS)
    description = models.TextField()


    status = models.CharField(
        max_length=1,
        choices=HOUSE_STATUS,
        blank=True,
        default='a',
        help_text='House Availability',
    )

    def get_absolute_url(self):
        """Returns the url to access a detail record for this house."""
        return reverse('house-detail', args=[str(self.house)]) # type: ignore

    def display_amenities(self):
        """Create a string for the amenities. This is required to display genre in Admin"""
        return ', '.join(amenity.name for amenity in self.amenities.all()[:3])

    display_amenities.short_description = 'Amenities'


    def __str__(self) -> str:
        return self.name


class HouseImages(models.Model):
    image_id = models.CharField(primary_key=True, default=gen_pk_image, max_length=50, editable=False)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    upload_pictures = models.ImageField(upload_to="house_images/")
