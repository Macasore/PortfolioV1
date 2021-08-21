from main.form import ContactForm
from django.contrib import admin
from django.urls import path
from .views import homeView, ContactMe

urlpatterns = [
    path('', homeView, name='home'),
    path('ajax/response/', ContactMe, name="contact_form"),
] 