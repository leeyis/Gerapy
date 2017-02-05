import os
from os import chdir
from os.path import dirname, exists, abspath

from .updateproject import update_project


def create_project(project):
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
            update_project(project)
    else:
        print('Exists')
        update_project(project)
