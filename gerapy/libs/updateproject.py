from os import chdir
from os.path import dirname, abspath


def update_project(project):
    path = dirname(dirname(abspath(__file__)))
    path = '{path}/storage/{project}/{project}'.format(path=path, project=project.name)
    try:
        update_items(path, project)
        update_pipelines(path, project)
        update_settings(path, project)
        update_spiders(path, project)
        update_cfg(path, project)
    except IOError:
        return False
    return True


def update_cfg(path, project):
    content = '''
[settings]
default = {project}.settings

[deploy]
url = http://localhost:6800/
project = {project}
    '''.format(project=project.name)
    update_file(path + '/../', 'scrapy.cfg', content)


def update_items(path, project):
    update_file(path, 'items.py', project.items)


def update_pipelines(path, project):
    update_file(path, 'pipelines.py', project.pipelines)


def update_settings(path, project):
    update_file(path, 'settings.py', project.settings)


def update_spiders(path, project):
    update_file(path + '/spiders', 'spiders.py', project.spiders)


def update_file(path, name, content):
    chdir(path)
    with open(name, 'w') as f:
        f.write(content)
        f.close()
