from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def page1(request):
    return HttpResponse("Страница 1 домашней работы 📓")


def page2(request):
    return HttpResponse("Страница 2 домашней работы 📓")
