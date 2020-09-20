"""Timekit.io REST API Python Client"""
from __future__ import absolute_import, unicode_literals
from timekit import components


class TimekitAPI:
    def __init__(self, app_token):
        self.apps = components.apps.App(app_token)
        self.bookings = components.bookings.Booking(app_token)
        self.projects = components.projects.Project(app_token)
        self.resources = components.resources.Resource(app_token)
