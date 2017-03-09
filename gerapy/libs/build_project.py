from os import chdir
from gerapy.libs.get_path import get_run_path


def build_project(project):
    path = get_run_path()
    path = '{path}/storage/{project}/{project}'.format(path=path, project=project.name)
    try:
        build_items(path, project)
        build_pipelines(path, project)
        build_settings(path, project)
        build_spiders(path, project)
        build_cfg(path, project)
    except IOError:
        return False
    return True


def build_cfg(path, project):
    content = '''
[settings]
default = {project}.settings

[deploy]
url = http://localhost:6800/
project = {project}
    '''.format(project=project.name)
    build_file(path + '/../', 'scrapy.cfg', content)


def build_items(path, project):
    build_file(path, 'items.py', project.items)


def build_pipelines(path, project):
    build_file(path, 'pipelines.py', project.pipelines)


def build_settings(path, project):
    settings ='''
BOT_NAME = '{name}'
SPIDER_MODULES = ['{name}.spiders']
NEWSPIDER_MODULE = '{name}.spiders'
'''.format(name=project.name)
    settings = project.settings + settings
    build_file(path, 'settings.py', settings)


def build_spiders(path, project):
    build_file(path + '/spiders', 'spiders.py', project.spiders)


def build_file(path, name, content):
    chdir(path)
    with open(name, 'w') as f:
        f.write(content)
        f.close()
