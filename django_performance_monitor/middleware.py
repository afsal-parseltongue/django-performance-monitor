
import logging
import time

from django.conf import settings

from .models import RequestLog, Config
from .constants import DEFAUL_LOG_THRESHOLD


logger = logging.getLogger(__name__)


class LogRequestMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        time_taken = time.time() - start
        if time_taken > request._log_threshold and Config.is_enabled():
            exclude_patterns = getattr(settings, "LOG_EXCLUDE_PATTERNS", [])
            for exclude_pattern in exclude_patterns:
                if exclude_pattern.match(request.path):
                    return response
            data = {
                "method": request.method,
                "path": request.path,
                "time_taken": time_taken,
                "meta_data": request.__dict__
            }
            RequestLog.objects.create(**data)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        request._log_threshold = self.get_log_threshold(view_func)
        return None

    def get_log_threshold(self, view_func):
        """
        get log_threshold from these settings:

            1. LOG_THRESHOLD attribute from View class
            2. LOG_THRESHOLD from settings
            3. default 1.5
        """
        if hasattr(view_func, "view_class"):
            if hasattr(view_func.view_class, "LOG_THRESHOLD"):
                return view_func.view_class.LOG_THRESHOLD
        return getattr(settings, "LOG_THRESHOLD", DEFAUL_LOG_THRESHOLD)
