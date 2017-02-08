from scrapyd_api import ScrapydAPI
from requests.exceptions import ConnectionError, InvalidURL

from .get_scrapyd import get_scrapyd


def schedule_spider(client, project_name, spider_name):
    try:
        scrapyd = get_scrapyd(client)
        result = scrapyd.schedule(project_name, spider_name)
        return result if result else False
    except (ConnectionError, InvalidURL):
        return False
