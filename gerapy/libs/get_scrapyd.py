from scrapyd_api import ScrapydAPI
from requests.exceptions import ConnectionError, InvalidURL


def get_scrapyd(client):
    url = 'http://{ip}:{port}'.format(ip=client.ip, port=client.port)
    try:
        scrapyd = ScrapydAPI(url)
        result = scrapyd.list_projects()
        return scrapyd
    except (ConnectionError, InvalidURL):
        return False