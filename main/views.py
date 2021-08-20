#sendemails/views.py
import django
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from .form import ContactForm
from django.core import serializers

def homeView(request):
    return render(request, "home.html")

def Contactform(request):
    if request.is_ajax and request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)
    return JsonResponse({"error": "" }, status=400)

def successViews(request):
    return HttpResponse('Success! Thank you for your message. I would reply shortly')
# Create your views here.
