from django.contrib import admin
from .models import LandLord, AgentAssignment

# Register your models here.
admin.site.register(LandLord)
admin.site.register(AgentAssignment)