"""test_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import time

from django.contrib import admin
from django.urls import path
from django.views.generic import View
from django.http import HttpResponse


class DelayView(View):

    def get(self, request, delay=0, *args, **kwarg):
        time.sleep(delay)
        return HttpResponse("ok")


class Within3sView(View):

    LOG_THRESHOLD = 3

    def get(self, request, delay=0, *args, **kwarg):
        time.sleep(delay)
        return HttpResponse("ok")


urlpatterns = [
    path("delay/<int:delay>/", DelayView.as_view()),
    path("with3s/<int:delay>/", Within3sView.as_view()),
    path('admin/', admin.site.urls),
]
