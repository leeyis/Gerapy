import configparser
import os

cwd = os.getcwd()

cf = configparser.ConfigParser()
cf.read(cwd + '/../gerapy.cfg')

def config(section, option):
    return cf.get(section, option)
