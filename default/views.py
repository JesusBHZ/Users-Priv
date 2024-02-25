from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse

def index(request):
    return render(request, 'index.html')