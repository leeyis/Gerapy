from scrapyd_api import ScrapydAPI
from requests.exceptions import ConnectionError, InvalidURL


def delete_version(project, client, version):
    url = 'http://{ip}:{port}'.format(ip=client.ip, port=client.port)
    try:
        scrapyd = ScrapydAPI(url)
        result = scrapyd.delete_version(project.name, version)
        return True if result else False
    except (ConnectionError, InvalidURL):
        return False
