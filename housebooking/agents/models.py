from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from home.models import User
from django.urls import reverse

#Unique ID Generator
ID_CHOICES = (
    ('NIN', 'NIN'),
    ('VIN', 'Voter\'s Card Num'),
)

OPTIONS = (
    ('yes', 'YES'),
    ('no', 'NO'),
)

class Agent(models.Model):
    agent = models.OneToOneField(User, on_delete=models.CASCADE)
    identification = models.CharField(max_length=16, choices=ID_CHOICES)
    id_number = models.CharField(max_length=20)
    DOB = models.DateField()
    licensing_organisation = models.CharField(max_length=200, blank=True)
    license_number = models.CharField(max_length=60, blank=True)
    upload_license = models.FileField(upload_to='agent_license/', blank=True)
    highest_academic_qualification = models.CharField(max_length=100, blank=True)
    education_institution = models.CharField(max_length=300, blank=True)
    upload_degree = models.FileField(upload_to='agent_degree/', blank=True)

    def get_absolute_url(self):
        """Takes you to the agent dashboard"""
        return reverse('agent_dashboard', args=[str(self.id)]) # type: ignore

    def __str__(self):
        return f"{self.agent.first_name} {self.agent.last_name}"

