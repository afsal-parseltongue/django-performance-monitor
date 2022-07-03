#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


import re

from django.test import TestCase


from django.test import Client
from django_performance_monitor.models import RequestLog


client = Client()


class RequestLogTest(TestCase):

    def setUp(self):
        pass

    def test_response(self):
        client.get("/delay/1/")
        client.get("/delay/2/")
        self.assertEqual(
            RequestLog.objects.count(),
            1
        )

    def test_setting(self):
        with self.settings(LOG_THRESHOLD=1):
            client.get("/delay/1/")
            client.get("/delay/2/")
            self.assertEqual(
                RequestLog.objects.count(),
                2
            )

    def test_customer_setting_work(self):
        with self.settings(LOG_THRESHOLD=1):
            client.get("/with3s/2/")
            self.assertEqual(
                RequestLog.objects.count(),
                0
            )

    def test_customer_setting_not_work(self):
        with self.settings(LOG_THRESHOLD=1):
            client.get("/with3s/3/")
            self.assertEqual(
                RequestLog.objects.count(),
                1
            )

    def test_exclude_patterns_work(self):
        with self.settings(LOG_EXCLUDE_PATTERNS=[re.compile("/exclude*")]):
            client.get("/exclude/3/")
            self.assertEqual(
                RequestLog.objects.count(),
                0
            )

    def test_exclude_patterns_not_work(self):
        with self.settings(LOG_EXCLUDE_PATTERNS=[ ]):
            client.get("/exclude/3/")
            self.assertEqual(
                RequestLog.objects.count(),
                1
            )
