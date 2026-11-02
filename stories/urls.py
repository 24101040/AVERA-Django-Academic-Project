from django.urls import path
from . import views

urlpatterns = [
    path('', views.stories_list, name='stories_list'),
    path('<int:id>/', views.story_details, name='story_details'),
]