import os
from os.path import dirname, abspath


def migrate(args):
    execute_path = os.getcwd()
    path = dirname(dirname(abspath(__file__)))
    os.chdir(path + '/webui')
    command = 'python3 manage.py ' + execute_path + ' makemigrations ' + args
    os.system(command)
    command = 'python3 manage.py ' + execute_path + ' migrate ' + args
    os.system(command)
