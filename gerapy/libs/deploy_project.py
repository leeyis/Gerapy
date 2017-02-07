import os
from os.path import dirname, abspath

import time
from scrapyd_api import ScrapydAPI

from gerapy.libs.check_project import get_egg_info


def deploy_project(project, client):
    path = dirname(dirname(abspath(__file__)))
    path = '{path}/storage/{project}/'.format(path=path, project=project.name)
    egg = get_egg_info(project)
    if egg:
        file_path = '{path}/{egg}'.format(path=path, egg=egg.get('name'))
        egg_file = open(file_path, 'rb')
        url = 'http://{ip}:{port}'.format(ip=client.ip, port=client.port)
        scrapyd = ScrapydAPI(url)
        version = str(time.time()).replace('.', '_')
        result = scrapyd.add_version(project.name, version, egg_file.read())
        return result, version
