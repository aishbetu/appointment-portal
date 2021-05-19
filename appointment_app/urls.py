from django.urls import path
from appointment_app import views

urlpatterns = [
    path('appointment', views.appointment, name='appointment'),
    path('success', views.success, name='success'),
]