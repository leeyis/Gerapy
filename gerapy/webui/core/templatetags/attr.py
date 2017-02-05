from django import template

register = template.Library()


def attr(obj, attr):
    return obj[attr]

register.filter('attr', attr)
