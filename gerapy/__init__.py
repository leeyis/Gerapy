import pymysql
pymysql.install_as_MySQLdb()


__version__ = '0.6.3'


def version():
    return __version__
