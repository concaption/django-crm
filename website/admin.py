"""
path: website/admin.py
description: Register Record model with admin site
"""

from django.contrib import admin
from .models import Record

admin.site.register(Record)
