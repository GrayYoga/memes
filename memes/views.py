from django.shortcuts import render
from django.http import HttpResponse  # added


def home(request):
    return HttpResponse('This is the home page.')
