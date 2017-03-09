from os.path import dirname, abspath

from gerapy.libs.get_path import get_package_path

path = get_package_path()


def get_settings():
    return get_content('/settings.py')


def get_items():
    return get_content('/items/template.py')


def get_middlewares():
    return get_content('/middlewares/template.py')


def get_pipelines():
    return get_content('/pipelines/template.py')

def get_content(file):
    try:
        with open(path + file, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return ''


if __name__ == '__main__':
    print(get_middlewares())
