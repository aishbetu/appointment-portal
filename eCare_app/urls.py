from django.urls import path
from eCare_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_us, name='contact_us'),
    path('about/', views.about_us, name='about_us'),
    path('update/', views.update, name='update'),
    path('tutorial/', views.tutorial, name='tutorial')
]