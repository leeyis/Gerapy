import os
import time
from gerapy.libs.get_path import get_run_path
from .date_format import date_format
from .pack_project import find_egg


def check_project(project, file):
    path = get_run_path()
    target = '{path}/storage/{project}/{file}'.format(path=path, project=project.name, file=file)
    try:
        update_time = os.stat(target).st_ctime
    except FileNotFoundError:
        return False
    now_time = time.time()
    if abs(now_time - update_time) < 2:
        return update_time
    return False


def get_egg_info(project):
    path = get_run_path()
    path = '{path}/storage/{project}/'.format(path=path, project=project.name)
    try:
        egg = find_egg(path)
        if egg:
            update_time = os.stat('{path}/{egg}'.format(path=path, egg=egg)).st_ctime
            return {'version': date_format(update_time, '%Y-%m-%d_%H_%M_%S'), 'name': egg}
        return None
    except FileNotFoundError:
        return None
