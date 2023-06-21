from django.urls import path
from . import views

urlpatterns = [
    path('create_agent/', views.AgentCreate.as_view(), name='create-agent'),
    path('update/<int:pk>/', views.AgentUpdate.as_view(), name='update-agent'), # type: ignore
    path('dashboard/<str:pk>/', views.dashboard, name="agent_dashboard"),

]
