from django.urls import path
from covid_test_app import views

urlpatterns = [
    path('covid_test', views.covid_test, name='covid_test'),
]