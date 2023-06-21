from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.TenantCreateView.as_view(), name='create-tenant'),
    path('dashboard/', views.dashboard, name="tenant_dashboard"),

]
