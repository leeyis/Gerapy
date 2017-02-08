from .spider import Spider
from .version import Version
from .job import Job
from requests.exceptions import ConnectionError, InvalidURL


class Project():
    def __init__(self, name, scrapyd):
        self.name = name
        self.scrapyd = scrapyd

    @property
    def jobs(self):
        try:
            jobs = self.scrapyd.list_jobs(self.name)
            statuses = ['running', 'pending', 'finished']
            for status in statuses:
                for job in jobs[status][::-1]:
                    yield Job(status, job.get('id'), job.get('start_time', ''),
                              job.get('end_time', ''), job.get('spider'), jobs.get('node_name', ''))
        except (ConnectionError, InvalidURL):
            return []

    @property
    def spiders(self):
        try:
            spiders = self.scrapyd.list_spiders(self.name)
            for spider in spiders:
                print(spider)
                yield Spider(spider)
        except (ConnectionError, InvalidURL):
            return []

    @property
    def versions(self):
        try:
            versions = self.scrapyd.list_versions(self.name)
            for version in versions:
                yield Version(version)
        except (ConnectionError, InvalidURL):
            return []

    @property
    def length(self):
        return len(self.jobs())

    @property
    def id(self):
        from .models import Project
        project = Project.objects.get(name=self.name)
        if project:
            return project.id
        return 0
