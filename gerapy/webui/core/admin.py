from django.contrib import admin

from .models import Client, Spider

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

class SpiderAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

admin.site.register(Client, ClientAdmin)
admin.site.register(Spider, SpiderAdmin)
