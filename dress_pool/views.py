from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def post_dress(request):
    return HttpResponse("Heelo World!!")
