import os
from os.path import dirname, abspath


def server(args):
    execute_path = os.getcwd()
    path = dirname(dirname(abspath(__file__)))
    os.chdir(path + '/webui')
    command = 'python3 manage.py ' + execute_path + ' runserver ' + args
    os.system(command)

