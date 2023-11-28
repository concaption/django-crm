"""
path: website/apps.py
description: Website app configuration
"""

from django.apps import AppConfig

class WebsiteConfig(AppConfig):
    """
    Website app configuration class
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "website"
