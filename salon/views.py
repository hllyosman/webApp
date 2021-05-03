from django.shortcuts import render
from django.http import HttpResponse
from .models import Staff

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    data = Staff.objects.all()
    params = {
        'data' : data,
    }
    return render(request, 'contact.html', params)