from time import strftime, localtime


def date_format(time, format='%Y-%m-%d %H:%M:%S'):
    return strftime(format, localtime(time))
