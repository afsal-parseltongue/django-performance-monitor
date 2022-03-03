
import time
import json

from django.conf import settings

from .models import RequestLog, Config
from .constants import DEFAUL_LOG_THRESHOLD


class LogRequestMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        time_taken = time.time() - start
        log_threshold = getattr(settings, "LOG_THRESHOLD", DEFAUL_LOG_THRESHOLD)
        if time_taken > log_threshold and Config.is_enabled():
            data = {
                "method": request.method,
                "path": request.path,
                "time_taken": time_taken,
                "meta_data": request.__dict__
            }
            RequestLog.objects.create(**data)
        return response
