import os
import subprocess

import time
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from scrapyd_api import ScrapydAPI
from gerapy.libs.check_project import check_project, get_egg_info
from gerapy.libs.date_format import date_format
from gerapy.libs.delete_version import delete_version
from gerapy.libs.deploy_project import deploy_project
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


def project_deploy(request, id, client_id):
    project = Project.objects.get(id=id)

    if request.method == 'GET':
        clients = Client.objects.order_by('-id')
        egg = get_egg_info(project)
        for client in clients:
            projects = client.projects
            if project.name in [project.name for project in projects]:
                client.deployed = True
            else:
                client.deployed = False
            client.connection = client.status
        return render(request, 'project/deploy.html', {
            'project': project,
            'clients': clients,
            'egg': egg
        })
    elif request.method == 'POST':
        client = Client.objects.get(id=client_id)
        result, deploy_version, egg_version = deploy_project(project, client)
        if result:
            return JsonResponse({
                'status': '1',
                'deploy_version': deploy_version,
                'egg_version': egg_version
            })
        return JsonResponse({'status': '0'})


def project_edit(request, id):
    if request.method == 'GET':
        project = Project.objects.get(id=id)
        return render(request, 'project/edit.html', {
            'project': project,
        })
    elif request.method == 'POST':
        project = Project.objects.filter(id=id)
        data = request.POST.dict()
        result = project.update(**data)
        if result:
            return JsonResponse({'status': '1'})
        return JsonResponse({'status': '0'})


def project_pack(request, id):
    project = Project.objects.get(id=id)
    start_project(project)
    egg = pack_project(project)
    check_result = check_project(project, egg)
    if check_result:
        result = {
            'name': egg,
            'status': '1',
            'version': date_format(check_result)
        }
        return JsonResponse(result)
    return JsonResponse({'status': '0'})


def version_delete(request, project_id, client_id):
    project = Project.objects.get(id=project_id)
    client = Client.objects.get(id=client_id)
    version = request.POST.get('version')
    if delete_version(project, client, version):
        return JsonResponse({'status': '1'})
    return JsonResponse({'status': '0'})
