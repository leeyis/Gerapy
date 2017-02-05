from requests.exceptions import InvalidURL
from .job import Job


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