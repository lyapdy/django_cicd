from django.test import TestCase
from rest_framework.test import APIClient

<<<<<<< HEAD
class TestSomething(TestCase):
    def test_ok(self):
        client = APIClient()
        response = client.get('api/v1/tests/')
        assert response.status_code == 200
=======

class TestSomething(TestCase):
    def test_ok(self):
        client = APIClient()
        response = client.get('/api/v1/test/')
        assert response.status_code == 200
>>>>>>> 9c3dd9c2a5fb527a84a3f9d9fe5e92455da0d086
