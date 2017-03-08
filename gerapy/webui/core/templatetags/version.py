from django import template
from requests.exceptions import InvalidURL, ConnectionError
from scrapyd_api import ScrapydAPI

register = template.Library()


def version(client, project):
    url = 'http://{ip}:{port}'.format(ip=client.ip, port=client.port)
    try:
        scrapyd = ScrapydAPI(url)
        versions = scrapyd.list_versions(project)
        if (len(versions) > 0):
            return versions[-1]
        return ''
    except (ConnectionError, InvalidURL, UnicodeError):
        return ''


register.filter('version', version)
