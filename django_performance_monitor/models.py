from django.db import models
from functools import lru_cache


class RequestLog(models.Model):
    path = models.TextField()
    method = models.CharField(max_length=255)
    time_taken = models.FloatField()
    meta_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f'{self.method} on the path {self.path} takes {self.time_taken}'


class Config(models.Model):
    is_active = models.BooleanField(default=True)

    def __str__(self):
        if self.is_active:
            return "Logging is active"
        return "Logging is inactive"

    def save(self, *args, **kwargs):
        is_already_exists = Config.objects.exists()
        if not is_already_exists or self.id:
            Config.is_enabled.cache_clear()
            super().save(args, **kwargs)

    @staticmethod
    @lru_cache(1)
    def is_enabled():
        config_obj = Config.objects.first()
        if not config_obj:
            return True
        return config_obj.is_active


