from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Staff, Contact
from .forms import ContactForm

def index(request):
    params = {
        'hp' : 'index',
    }
    return render(request, 'index.html', params)

def contact(request):
    if (request.method == 'POST'):
        params = {
            'hp' : 'index',
            'message' : 'message'
        }
        obj =Contact()
        contact = ContactForm(request.POST, instance=obj)
        contact.save()
        return render(request, 'contact.html', params)
    else:
        params = {
            'hp' : 'index',
            'form' : ContactForm(),
        }
        return render(request, 'contact.html', params)

def message(request, num=1):
    data = Contact.objects.all().reverse()
    page = Paginator(data, 5)
    params = {
        'hp' : 'index',
        'data' : page.get_page(num),
    }
    return render(request, 'message.html', params)