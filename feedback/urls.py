from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_list, name='feedback_list'),
    path('add/', views.feedback_create, name='feedback_create'),
    path('edit/<int:pk>/', views.feedback_update, name='feedback_update'),  # এই লাইনটি যুক্ত করুন
    path('delete/<int:pk>/', views.feedback_delete, name='feedback_delete'), # এই লাইনটি যুক্ত করুন
]