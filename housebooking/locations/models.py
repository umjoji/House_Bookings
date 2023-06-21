from django.db import models
import uuid

# Create your models here.

def gen_pk_state():
    return f"STA-{uuid.uuid4().hex[:5].upper()}"

def gen_pk_city():
    return f"CIT-{uuid.uuid4().hex[:5].upper()}"

def gen_pk_country():
    return f"NAT-{uuid.uuid4().hex[:5].upper()}"

class Country(models.Model):
    country_id = models.CharField(primary_key=True, default=gen_pk_state, max_length=50, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class State(models.Model):
    state_id = models.CharField(primary_key=True, default=gen_pk_state, max_length=50, editable=False)
    name = models.CharField(max_length=100)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class City(models.Model):
    city_id = models.CharField(primary_key=True, default=gen_pk_city, max_length=50, editable=False)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE) # type: ignore
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name