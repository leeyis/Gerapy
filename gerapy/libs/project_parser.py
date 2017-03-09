import configparser
import os

cwd = os.environ.get('DJANGO_RUN_PATH')
cf = configparser.ConfigParser()
cfg_path = cwd + '/gerapy.cfg'
cf.read(cfg_path)

def config(section, option, default=None):
    try:
        return cf.get(section, option)
    except configparser.NoOptionError:
        return default

def path():
    return cfg_path