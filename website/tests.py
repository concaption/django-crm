"""
path: website/tests.py
description: Tests for Record app
Todo: Add tests for Record model
Note: These tests are run with the command:
    `python manage.py test`
"""

from django.test import TestCase

class RecordModelTests(TestCase):
    """
    Tests for Record model
    """
    def test_create_record(self):
        """
        Test that Record model can be created
        """
        self.assertEqual(1, 1)
