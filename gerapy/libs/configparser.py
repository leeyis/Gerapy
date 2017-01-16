import configparser
from os.path import *

cwd = dirname(dirname(dirname(abspath(__file__))))


cf = configparser.ConfigParser()
cfg_path = cwd + '/gerapy.cfg'
cf.read(cfg_path)


def config(section, option):
    return cf.get(section, option)