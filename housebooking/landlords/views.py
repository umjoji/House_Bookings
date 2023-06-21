from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import LandLord
from django.views.generic import ListView, TemplateView, FormView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from home.models import User
from .forms import UserCreateForm
from django.contrib.auth import login
from django.contrib.auth import models
from django.http import HttpResponse

# Create your views here.

class LandLordListView(ListView):
    model = LandLord
    paginate_by = 10

class LandLordDetailView(DetailView):
    model = LandLord

class LandlordCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'landlords/landlord_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'landlord'
        return super().get_context_data(**kwargs)

    def form_valid(self, form) -> HttpResponse:
        user = form.save()
        login(self.request, user) # type: ignore
        return redirect('index')

class LandLordUpdate(UpdateView):
    model = LandLord
    fields = ['identification', 'id_number', 'DOB', 'evidence_of_ownership',
              'do_you_own_the_home']

def dashboard(request, pk):
    return render(request, "dashboard_landlord.html")