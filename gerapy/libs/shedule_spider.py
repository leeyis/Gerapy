from scrapyd_api import ScrapydAPI
from requests.exceptions import ConnectionError, InvalidURL


def schedule_spider(client, project_name, spider_name):
    url = 'http://{ip}:{port}'.format(ip=client.ip, port=client.port)
    try:
        scrapyd = ScrapydAPI(url)
        result = scrapyd.schedule(project_name, spider_name)
        return result if result else False
    except (ConnectionError, InvalidURL):
        return False
