from django.urls import path
from .views import adoption_hub

urlpatterns = [
    path('', adoption_hub, name='adoption_hub'),
]