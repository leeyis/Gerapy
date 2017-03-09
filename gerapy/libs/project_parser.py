import configparser
import os

cwd = os.environ.get('DJANGO_RUN_PATH')
cf = configparser.ConfigParser()
cfg_path = cwd + '/gerapy.cfg'
cf.read(cfg_path)

def config(section, option):
    return cf.get(section, option)

def path():
    return cfg_path