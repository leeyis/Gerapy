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



def projects(request):
    projects = Spider.objects.all()
    return render(request, 'project/index.html', {
        'projects': projects
    })


def project(request, id):
    if request.method == 'GET':
        project = Spider.objects.get(id=id)
        return render(request, 'project/show.html', {
            'project': project
        })
    elif request.method == 'POST':
        project = Spider.objects.filter(id=id)
        data = request.POST.dict()
        project.update(**data)
        return HttpResponseRedirect(reverse('project_edit', args=[id]))

def project_edit(request, id):
    project = Spider.objects.get(id=id)
    return render(request, 'project/edit.html', {
        'project': project
    })