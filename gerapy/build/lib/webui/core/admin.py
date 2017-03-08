from django.contrib import admin
from .models import Client, Project


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip', 'port', 'created_at')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')


admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)
