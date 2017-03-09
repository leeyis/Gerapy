import os
from os import chdir
from os.path import dirname, exists, abspath
from gerapy.libs.get_path import get_run_path
from .build_project import build_project


def start_project(project):
    path = get_run_path()
    target = path + '/storage/'
    try:
        chdir(target)
    except FileNotFoundError:
        os.mkdir(target)
        chdir(target)
    result = exists(target + project.name)
    if not result:
        result = os.system('scrapy3 startproject ' + project.name)
        if not result == 0:
            result = os.system('scrapy startproject ' + project.name)
        if not result == 0:
            print('Create Project Failed')
        else:
            build_project(project)
    else:
        print('Exists')
        build_project(project)
