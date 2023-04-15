from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def goToMap(request):
    return render(request, 'main/map.html')