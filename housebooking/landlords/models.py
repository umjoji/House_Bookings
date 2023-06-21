from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from agents.models import Agent
from home.models import User
from django.urls import reverse

#Unique ID Generator
ID_CHOICES = (
    ('NIN', 'NIN'),
    ('VIN', "Voter's Card Num"),
)

OPTIONS = (
    ('yes', 'YES'),
    ('no', 'NO'),
)


class LandLord(models.Model):
    landlord = models.OneToOneField(User, on_delete=models.CASCADE)
    identification = models.CharField(max_length=16, choices=ID_CHOICES)
    id_number = models.CharField(max_length=20)
    DOB = models.DateField(blank=True)
    evidence_of_ownership = models.FileField(upload_to='house_evidence/', blank=True)
    do_you_own_the_home = models.CharField(max_length=10, choices=OPTIONS)
    phone_number = models.CharField(max_length=11, blank=True)

    def get_absolute_url(self):
        """Takes you to the landlord dashboard."""
        return reverse('landlord_detail', args=[str(self.id)]) # type: ignore

    def __str__(self):
        return f"{self.landlord.first_name} {self.landlord.last_name}"

class AgentAssignment(models.Model):
    landlord = models.ForeignKey(LandLord, default=None, on_delete=models.CASCADE)
    agent = models.ManyToManyField(Agent, help_text="Assign an agent to this client.")
    agent_assigned_date = models.DateField(auto_now=True)
