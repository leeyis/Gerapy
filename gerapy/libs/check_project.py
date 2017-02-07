import os
from os import chdir
from os.path import dirname, abspath

import time


def check_project(project, file):
    path = dirname(dirname(abspath(__file__)))
    target = '{path}/storage/{project}/{file}'.format(path=path, project=project.name, file=file)
    try:
        change_time = os.stat(target).st_ctime
    except FileNotFoundError:
        return False
    now_time = time.time()
    if abs(now_time - change_time) < 2:
        return True
    return False
