from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    is_tenant = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    is_landlord = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.get_full_name()
