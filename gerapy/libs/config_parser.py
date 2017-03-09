import configparser
from os.path import *

cwd = dirname(dirname(abspath(__file__)))

cf = configparser.ConfigParser()
cfg_path = cwd + '/setup.cfg'
cf.read(cfg_path)

def config(section, option):
    return cf.get(section, option)