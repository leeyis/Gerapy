import configparser
from os.path import *

cwd = dirname(dirname(abspath(__file__)))

cf = configparser.ConfigParser()
cfg_path = cwd + '/setup.cfg'
cf.read(cfg_path)

def config(section, option, default=None):
    try:
        return cf.get(section, option)
    except configparser.NoOptionError:
        return default
