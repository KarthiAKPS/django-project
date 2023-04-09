from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    
    deslist = Destination.objects.all()
    
    return render(request, 'index.html', {'deslist' : deslist})

def Kerala(request):
    
    deslist = Destination.objects.all()
    
    return render(request, 'Kerala.html', {'deslist' : deslist})

def Chennai(request):
    
    deslist = Destination.objects.all()
    
    return render(request, 'Chennai.html', {'deslist' : deslist})

def Rajasthan(request):
    
    deslist = Destination.objects.all()
    
    return render(request, 'Rajasthan.html', {'deslist' : deslist})