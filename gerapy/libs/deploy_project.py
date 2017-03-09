import os
from os.path import dirname, abspath

import time
from scrapyd_api import ScrapydAPI
from requests.exceptions import ConnectionError, InvalidURL

from gerapy.libs.check_project import get_egg_info
from gerapy.libs.get_path import get_run_path
from .date_format import date_format


def deploy_project(project, client):
    path = get_run_path()
    path = '{path}/storage/{project}/'.format(path=path, project=project.name)
    egg = get_egg_info(project)
    if egg:
        file_path = '{path}/{egg}'.format(path=path, egg=egg.get('name'))
        egg_file = open(file_path, 'rb')
        deploy_version = date_format(time.time(), '%Y-%m-%d_%H_%M_%S')
        url = 'http://{ip}:{port}'.format(ip=client.ip, port=client.port)
        try:
            scrapyd = ScrapydAPI(url)
            egg_version = egg.get('version')
            result = scrapyd.add_version(project.name, deploy_version, egg_file.read())
            return result, deploy_version, egg_version
        except (ConnectionError, InvalidURL):
            return None, None, None
