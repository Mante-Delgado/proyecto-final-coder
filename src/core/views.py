from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def saludar(request):
    return HttpResponse("Hola desde Django")