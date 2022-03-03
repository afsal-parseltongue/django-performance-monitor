from django.contrib import admin

from .models import RequestLog, Config


admin.site.register(RequestLog)
admin.site.register(Config)