import getopt
import os
import sys
from os.path import dirname, abspath
from optparse import OptionParser

from os import chdir

import gerapy
from gerapy.libs.get_content import get_content


def version():
    print(gerapy.version())


def run(args):
    execute_path = os.getcwd()
    print(execute_path)
    path = dirname(dirname(abspath(__file__)))
    chdir(path + '/webui')
    command = 'python3 manage.py ' + execute_path + ' runserver ' + args
    os.system(command)


def create(args):
    os.mkdir(args)
    os.chdir(args)
    with open('gerapy.cfg', 'w') as f:
        f.write(get_content('/gerapy.cfg'))
        f.close()


def main():
    parser = OptionParser()
    parser.add_option('-v', '--version', action='store_true', help='show version of gerapy')
    parser.add_option('-r', '--run', action='store_true', help='run webui', default='')
    parser.add_option('-c', '--create', action='store_true', help='create project', default='')
    options, args = parser.parse_args(sys.argv)
    print(options, args)
    if options.version:
        version()
    if options.run:
        run(args[1] if len(args) >= 2 else '')
    if options.create:
        create(args[1] if len(args) >= 2 else '')
