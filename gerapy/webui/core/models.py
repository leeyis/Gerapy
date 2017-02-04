from django.db.models import Model, CharField, DateTimeField, TextField


class Spider(Model):
    name = CharField(max_length=255, default=None)
    code = TextField(default=None, blank=True)
    settings = TextField(default=None, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class Client(Model):
    name = CharField(max_length=255, default=None)
    ip = CharField(max_length=255, default=None, blank=True)
    description = TextField(default=None, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
