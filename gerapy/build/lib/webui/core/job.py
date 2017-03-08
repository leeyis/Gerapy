

class Job():
    def __init__(self, status, id, start_time, end_time, spider, node_name):
        self.status = status
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.spider = spider
        self.node_name = node_name