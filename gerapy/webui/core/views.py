import json
import os
import subprocess

import time

import requests
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from scrapyd_api import ScrapydAPI

from gerapy.libs.cancel_job import cancel_job
from gerapy.libs.check_project import check_project, get_egg_info
from gerapy.libs.date_format import date_format
from gerapy.libs.delete_version import delete_version
from gerapy.libs.deploy_project import deploy_project
from gerapy.libs.get_scrapyd import get_scrapyd
from gerapy.libs.shedule_spider import schedule_spider
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


def client_edit(request, id):
    if request.method == 'GET':
        client = Client.objects.get(id=id)
        return render(request, 'client/edit.html', {
            'client': client
        })
    elif request.method == 'POST':
        client = Client.objects.filter(id=id)
        data = request.POST.dict()
        client.update(**data)
        return HttpResponseRedirect(reverse('client', args=[id]))


def client_schedule(request, id):
    if request.method == 'GET':
        client = Client.objects.get(id=id)
        return render(request, 'client/schedule.html', {
            'client': client
        })


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


def project_jobs(request, client_id):
    from .project import Project
    project_name = request.POST.get('project_name')
    client = Client.objects.get(id=client_id)
    scrapyd = get_scrapyd(client)
    project = Project(project_name, scrapyd)
    return render(request, 'client/jobs.html', {
        'project': project,
        'client': client
    })


def version_delete(request, project_id, client_id):
    project = Project.objects.get(id=project_id)
    client = Client.objects.get(id=client_id)
    version = request.POST.get('version')
    if delete_version(project, client, version):
        return JsonResponse({'status': '1'})
    return JsonResponse({'status': '0'})


def spider_schedule(request, id):
    client = Client.objects.get(id=id)
    project_name = request.POST.get('project_name')
    spider_name = request.POST.get('spider_name')
    result = schedule_spider(client, project_name, spider_name)
    if result:
        return JsonResponse({'status': '1'})
    return JsonResponse({'status': '0'})


def job_cancel(request, id):
    client = Client.objects.get(id=id)
    project_name = request.POST.get('project_name')
    job_id = request.POST.get('job_id')
    result = cancel_job(client, project_name, job_id)
    if result:
        return JsonResponse({'status': '1'})
    return JsonResponse({'status': '0'})


def job_log(request, id):
    client = Client.objects.get(id=id)
    project_name = request.POST.get('project_name')
    spider_name = request.POST.get('spider_name')
    job_id = request.POST.get('job_id')
    # http://localhost:6800/logs/quotesbot/toscrape-css/472499baede711e6befaa0999b0d6843.log
    url = 'http://{ip}:{port}/logs/{project_name}/{spider_name}/{job_id}.log'. \
        format(ip=client.ip, port=client.port,
               project_name=project_name,
               spider_name=spider_name,
               job_id=job_id)
    response = requests.get(url)
    if response.status_code == 200:
        return JsonResponse({'status': '1', 'content': response.text})
    return JsonResponse({'status': '0'})
