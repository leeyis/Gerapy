import os
from os.path import dirname, abspath


def get_package_path():
    return dirname(dirname(abspath(__file__)))


def get_run_path():
    return os.getcwd()


if __name__ == '__main__':
    print(get_run_path())