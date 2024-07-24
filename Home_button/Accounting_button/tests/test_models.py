# Accounting_button/tests/test_models.py
from django.test import TestCase
from .factories import ExecutorPositionFactory

class ExecutorPositionModelTest(TestCase):
    def setUp(self):
        self.developer = ExecutorPositionFactory(position="Developer", comment="Develops software")
        self.manager = ExecutorPositionFactory(position="Manager", comment="Manages projects")

    def test_position_creation(self):
        self.assertEqual(self.developer.comment, "Develops software")
        self.assertEqual(self.manager.comment, "Manages projects")

    def test_str_representation(self):
        position = ExecutorPositionFactory(position="Designer")
        self.assertEqual(str(position), "Designer")
