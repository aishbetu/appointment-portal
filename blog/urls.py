from django.urls import path
from .views import blog, read_article

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('blog/<str:slug>', read_article),
]