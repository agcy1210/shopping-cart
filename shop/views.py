from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product

def index(request):
    return HttpResponse('test view')
