from main.form import ContactForm
from django.contrib import admin
from django.urls import path
from .views import homeView, successViews,ContactForm

urlpatterns = [
    path('', homeView, name='home'),
    path('ajax/response', ContactForm, name="contact_form"),
    path('success/', successViews, name='success'),
] 