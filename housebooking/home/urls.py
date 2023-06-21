from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('register/', views.register_view, name='create-user'), # type: ignore
    path('user/<int:pk>/', views.preview_user, name='user-detail'),
    path('about/', views.about_us, name="about"),

]
