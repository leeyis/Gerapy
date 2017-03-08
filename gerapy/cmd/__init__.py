import getopt
import os
import sys
from os.path import dirname, abspath
from optparse import OptionParser

from os import chdir

import gerapy


def version():
    print(gerapy.version())


def run(args):
    path = dirname(dirname(abspath(__file__)))
    chdir(path + '/webui')
    print('sssss')
    command = 'python3 manage.py runserver ' + args
    print(command)
    os.system(command)


def main():
    parser = OptionParser()
    parser.add_option('-v', '--version', action='store_true', help='show version of gerapy')
    parser.add_option('-r', '--run', action='store_true', help='run webui', default='')
    options, args = parser.parse_args(sys.argv)

    if options.version:
        version()
    if options.run:
        run(args[1] if len(args) >= 2 else '')
