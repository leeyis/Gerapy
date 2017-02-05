from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import Spider, Client


def index(request):
    latest_question_list = Spider.objects.all()
    return render(request, 'index.html')



def clients(request):
    clients = Client.objects.all()
    return render(request, 'client/index.html', {
        'clients': clients
    })


def client(request, id):
    if request.method == 'GET':
        client = Client.objects.get(id=id)
        return render(request, 'client/show.html', {
            'client': client
        })
    elif request.method == 'POST':
        client = Client.objects.filter(id=id)
        data = request.POST.dict()
        client.update(**data)
        return HttpResponseRedirect(reverse('client', args=[id]))



def spiders(request):
    spiders = Spider.objects.all()
    return render(request, 'spider/index.html', {
        'spiders': spiders
    })


def spider(request, id):
    if request.method == 'GET':
        spider = Spider.objects.get(id=id)
        return render(request, 'spider/show.html', {
            'spider': spider
        })
    elif request.method == 'POST':
        spider = Spider.objects.filter(id=id)
        data = request.POST.dict()
        spider.update(**data)
        return HttpResponseRedirect(reverse('spider_edit', args=[id]))

def spider_edit(request, id):
    spider = Spider.objects.get(id=id)
    return render(request, 'spider/edit.html', {
        'spider': spider
    })