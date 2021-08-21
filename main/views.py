#sendemails/views.py
import json
import django
from django.core.mail import message, send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from .models import Contact
from .form import ContactForm
from django.core import serializers

def homeView(request):
    return render(request, "home.html")

def ContactMe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        response_data = {}

        contact = Contact(name=name,email=email,subject=subject,message=message)
        contact.save()

        response_data['result'] = 'Sucess'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json")
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

