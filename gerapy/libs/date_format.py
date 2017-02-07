from time import strftime, localtime


def date_format(time):
    return strftime('%Y-%m-%d %H:%M:%S', localtime(time))
