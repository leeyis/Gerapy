import os
from os import chdir
from os.path import dirname, abspath

import time


def check_project(project):
    path = dirname(dirname(abspath(__file__)))
    path = '{path}/storage/{project}/{project}/spiders/'.format(path=path, project=project.name)
    chdir(path)
    change_time = os.stat(path + 'spiders.py').st_ctime
    now_time = time.time()
    if abs(now_time - change_time) < 2:
        return True
    return False
