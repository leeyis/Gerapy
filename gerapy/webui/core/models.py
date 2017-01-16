from django.db.models import Model, CharField, DateTimeField, ForeignKey, IntegerField, TextField


# Create your models here.

class Spider(Model):
    name = CharField(max_length=255)
    allowed_domains = TextField(default=None, blank=True)
    start_urls = TextField(default=None, blank=True)
    custom_settings = TextField(default=None, blank=True)
    methods = TextField(default=None, blank=True)
    crawler = TextField(default=None, blank=True)
    settings = TextField(default=None, blank=True)
    logger = CharField(max_length=255, default=None, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class Rule(Model):
    allow = TextField(default=None, blank=True)
    deny = TextField(default=None, blank=True)
    allow_domains = TextField(default=None, blank=True)
    deny_domains = TextField(default=None, blank=True)
    deny_extensions = TextField(default=None, blank=True)
    restrict_xpaths = TextField(default=None, blank=True)
    restrict_css = TextField(default=None, blank=True)
    tags = TextField(default=None, blank=True)
    attrs = TextField(default=None, blank=True)
    canonicalize = IntegerField(default=1, blank=True)
    unique = IntegerField(default=1, blank=True)
    process_value = CharField(max_length=255, blank=True)
    callback = CharField(max_length=255, blank=True)
    cb_kwargs = TextField(default=None, blank=True)
    follow = IntegerField(default=0, blank=True)
    process_links = CharField(max_length=255, blank=True)
    process_request = CharField(max_length=255, blank=True)
    created_at = DateTimeField(auto_now_add=True, blank=True)
    updated_at = DateTimeField(auto_now=True, blank=True)
    spider = ForeignKey(Spider)
