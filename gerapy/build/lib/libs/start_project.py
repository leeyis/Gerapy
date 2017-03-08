import os
from os import chdir
from os.path import dirname, exists, abspath

from .build_project import build_project


def start_project(project):
    path = dirname(dirname(abspath(__file__)))
    chdir(path + '/storage')
    result = exists(path + '/storage/' + project.name)
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
