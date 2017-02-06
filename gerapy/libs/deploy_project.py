import os
from os import chdir
from os.path import dirname, abspath

import time

import shutil


def deploy_project(project):
    '''
     path = dirname(dirname(abspath(__file__)))
    path = '{path}/storage/{project}/{project}/spiders/'.format(path=path, project=project.name)
    chdir(path)
    change_time = os.stat(path + 'spiders.py').st_ctime
    now_time = time.time()
    if abs(now_time - change_time) < 2:
        return True
    return False


    '''
    egg = build_egg(project)
    print(egg)


import sys
import os
import glob
import tempfile
from subprocess import check_call
from scrapy.utils.python import retry_on_eintr
from scrapy.utils.conf import get_config

_SETUP_PY_TEMPLATE = \
"""
# Automatically created by: scrapyd-deploy

from setuptools import setup, find_packages

setup(
    name         = '%(project)s',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = %(settings)s']},
)"""


def build_egg(project):
    path = dirname(dirname(abspath(__file__)))
    path = '{path}/storage/{project}/'.format(path=path, project=project.name)
    os.chdir(path)
    settings = get_config().get('settings', 'default')
    _create_default_setup_py(settings=settings, project=project.name)
    d = tempfile.mkdtemp(prefix="scrapydeploy-")
    o = open(os.path.join(d, "stdout"), "wb")
    e = open(os.path.join(d, "stderr"), "wb")
    retry_on_eintr(check_call, [sys.executable, 'setup.py', 'clean', '-a', 'bdist_egg', '-d', d], stdout=o, stderr=e)
    o.close()
    e.close()
    egg = glob.glob(os.path.join(d, '*.egg'))[0]
    os.system('rm *.egg')
    shutil.move(egg, path)
    return find_egg(path)


def find_egg(path):
    items = os.listdir(path)
    for names in items:
        if names.endswith(".egg"):
            return names


def _create_default_setup_py(**kwargs):
    with open('setup.py', 'w') as f:
        f.write(_SETUP_PY_TEMPLATE % kwargs)
        f.close()
