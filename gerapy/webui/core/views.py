import os
import subprocess

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

from gerapy.libs.check_project import check_project, get_egg_info
from gerapy.libs.date_format import date_format
from gerapy.libs.start_project import start_project
from gerapy.libs.pack_project import pack_project
from .models import Project, Client


def index(request):
    latest_question_list = Project.objects.all()
    return render(request, 'index.html')


def clients(request):
    clients = Client.objects.order_by('-id')
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


def client_create(request):
    if request.method == 'POST':
        Client.objects.create(**request.POST.dict())
    return HttpResponseRedirect(reverse('clients'))


def projects(request):
    projects = Project.objects.order_by('-id')
    return render(request, 'project/index.html', {
        'projects': projects
    })


def project_create(request):
    if request.method == 'POST':
        Project.objects.create(**request.POST.dict())
    return HttpResponseRedirect(reverse('projects'))


def project_deploy(request, id):
    project = Project.objects.get(id=id)
    egg = get_egg_info(project)
    return render(request, 'project/deploy.html', {
        'project': project,
        'egg': egg
    })


def project_edit(request, id):
    if request.method == 'GET':
        project = Project.objects.get(id=id)
        return render(request, 'project/edit.html', {
            'project': project,
        })
    elif request.method == 'POST':
        project = Project.objects.filter(id=id)
        data = request.POST.dict()
        project.update(**data)
        return HttpResponseRedirect(reverse('project_edit', args=[id]))


def project_pack(request, id):
    project = Project.objects.get(id=id)
    start_project(project)
    egg = pack_project(project)
    check_result = check_project(project, egg)
    if check_result:
        result = {
            'name': egg,
            'status': '1',
            'update_time': date_format(check_result)
        }
        return JsonResponse(result)
    return HttpResponse({'status': '0'})
