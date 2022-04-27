from unittest import TestCase


from django.test import TestCase

class ControllerTest(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def test_for_valid_data_input(self):
        """Data as required to be answered by SME"""
        self.assertEqual(True,True)