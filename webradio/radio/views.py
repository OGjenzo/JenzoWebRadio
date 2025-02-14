# Create your views here.
from django.shortcuts import render
from .models import Stream

def index(request):
    streams = Stream.objects.all()
    return render(request, "radio/index.html", {"streams": streams})
