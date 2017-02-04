from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Spider, Client


def index(request):
    latest_question_list = Spider.objects.all()
    return render(request, 'index.html')



def clients(request):
    clients = Client.objects.all()
    return render(request, 'client/index.html', {
        'clients': clients
    })


def clients(request, id):
    client = Client.objects.get(id=id)
    return render(request, 'client/show.html', {
        'client': client
    })