from django.db.models import Model, CharField, DateTimeField, TextField, IntegerField, GenericIPAddressField
from scrapyd_api import ScrapydAPI
from requests.exceptions import ConnectionError, InvalidURL


class Project(Model):
    name = CharField(max_length=255, default=None)
    description = CharField(max_length=255, default='', blank=True)
    spiders = TextField(default='', blank=True)
    settings = TextField(default='', blank=True)
    items = TextField(default='', blank=True)
    middlewares = TextField(default='', blank=True)
    pipelines = TextField(default='', blank=True)
    tools = TextField(default='', blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class Client(Model):
    name = CharField(max_length=255, default=None)
    ip = GenericIPAddressField(max_length=255, default='')
    port = IntegerField(default=6800, blank=True)
    description = TextField(default='', blank=True)
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
        except (ConnectionError, InvalidURL, UnicodeError):
            return {
                'class': 'danger',
                'text': '连接错误',
                'symbol': 0
            }
        else:
            return {
                'class': 'primary',
                'text': '运行正常',
                'symbol': 1
            }

    @property
    def projects(self):
        from .project import Project
        try:
            projects = self.scrapyd.list_projects()
        except (ConnectionError, InvalidURL, UnicodeError):
            return []
        else:
            for project in projects:
                yield Project(project, self.scrapyd)
