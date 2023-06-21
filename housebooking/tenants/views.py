from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tenant
from django.urls import reverse
from .forms import UserCreateForm
from home.models import User
from django.contrib.auth import login
from django.contrib.auth import models

# Create your views here.

# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreateForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             fm = form.save(commit=False)
#             fm.save()
#             form = UserCreateForm()
#         return render(request, 'index.html', {'form': form})
#     else:
#         form = UserCreateForm()
#         context = {'form': form,}
#     return render(request, 'auth/user_form.html', {'form': form})

class TenantCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'tenants/tenant_form.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        kwargs['user_type'] = 'tenant'
        return super().get_context_data(**kwargs)

    def form_valid(self, form) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        return redirect('index')

class TenantUpdate(UpdateView):
    model = Tenant
    fields = ['identification',
              'id_number',
              'DOB',
    ]

    def form_valid(self, form):
        form.instance.tenant = self.request.user
        return super().form_valid(form)

def dashboard(request):
    return render(request, "dashboard_tenant.html")