from django.contrib import admin

from .models import RequestLog, Config


class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('method', 'path', 'time_taken')


admin.site.register(RequestLog, RequestLogAdmin)
admin.site.register(Config)