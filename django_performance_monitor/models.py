from django.db import models


class RequestLog(models.Model):
    path = models.TextField()
    method = models.CharField(max_length=255)
    time_taken = models.FloatField()
    meta_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f'{self.method} on the path {self.path} takes {self.time_taken}'
