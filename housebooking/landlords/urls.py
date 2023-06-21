from django.urls import path
from . import views

urlpatterns = [
    path('create_landlord/', views.LandlordCreateView.as_view(), name='create-landlord'),
    path('update_landlord/<str:pk>/', views.LandLordUpdate.as_view(), name='update-landlord'),
    path('all/', views.LandLordListView.as_view(), name='landlords'),
    path('<str:pk>/', views.LandLordDetailView.as_view(), name='landlord-detail'),
    path('dashboard/<str:pk>/', views.dashboard, name="landlord_dashboard"),

]

