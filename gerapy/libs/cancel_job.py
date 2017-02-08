from scrapyd_api import ScrapydAPI
from requests.exceptions import ConnectionError, InvalidURL
from .get_scrapyd import get_scrapyd


def cancel_job(client, project_name, job_id):
    try:
        scrapyd = get_scrapyd(client)
        result = scrapyd.cancel(project_name, job_id)
        return result if result else False
    except (ConnectionError, InvalidURL):
        return False
