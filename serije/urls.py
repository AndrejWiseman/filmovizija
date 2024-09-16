from django.urls import path
from .views import serije

urlpatterns = [
    path('serije/', serije)
]