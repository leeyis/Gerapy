from django.db.models import Model, CharField, DateTimeField, TextField, IntegerField, GenericIPAddressField
from requests.packages.urllib3 import HTTPConnectionPool
from scrapyd_api import ScrapydAPI
from requests.exceptions import ConnectionError, InvalidURL


class Spider(Model):
    name = CharField(max_length=255, default=None)
    code = TextField(default=None, blank=True)
    settings = TextField(default=None, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class Client(Model):
    name = CharField(max_length=255, default=None)
    ip = GenericIPAddressField(max_length=255, default=None)
    port = IntegerField(default=6800, blank=True)
    description = TextField(default=None, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    @property
    def scrapyd(self):
        url = 'http://{ip}:{port}'.format(ip=self.ip, port=self.port)
        return ScrapydAPI(url)

    @property
    def status(self):
        try:
            self.scrapyd.list_projects()
        except (ConnectionError, InvalidURL):
            return {
                'class': 'danger',
                'text': '连接错误'
            }
        else:
            return {
                'class': 'primary',
                'text': '运行正常'
            }

    @property
    def projects(self):
        try:
            projects = self.scrapyd.list_projects()
        except (ConnectionError, InvalidURL):
            return []
        else:
            for project in projects:
                yield Project(project, self.scrapyd)


class Project():
    def __init__(self, name, scrapyd):
        self.name = name
        self.scrapyd = scrapyd

    @property
    def jobs(self):
        try:
            jobs = self.scrapyd.list_jobs(self.name)
            print(jobs)
            statuses = ['running', 'pending', 'finished']
            for status in statuses:
                for job in jobs[status]:
                    yield Job(status, job['id'], job['start_time'], job['end_time'], job['spider'], jobs['node_name'])
        except (ConnectionError, InvalidURL):
            return []

    @property
    def length(self):
        return len(self.jobs())


class Job():
    def __init__(self, status, id, start_time, end_time, spider, node_name):
        self.status = status
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.spider = spider
        self.node_name = node_name
