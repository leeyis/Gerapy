import sys
from optparse import OptionParser
from gerapy.cmd.create import create
from gerapy.cmd.server import server
from gerapy.cmd.version import version
from gerapy.cmd.migrate import migrate


def main():
    parser = OptionParser()
    parser.add_option('-v', '--version', action='store_true', help='show version of gerapy')
    parser.add_option('-s', '--server', action='store_true', help='run webui server', default='')
    parser.add_option('-c', '--create', action='store_true', help='create project', default='')
    parser.add_option('-m', '--migrate', action='store_true', help='create database and migrate', default='')
    options, args = parser.parse_args(sys.argv)
    if options.version:
        version()
    if options.server:
        server(args[1] if len(args) >= 2 else '')
    if options.create:
        create(args[1] if len(args) >= 2 else '')
    if options.migrate:
        migrate(args[1] if len(args) >= 2 else '')
