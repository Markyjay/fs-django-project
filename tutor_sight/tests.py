from django.test import TestCase

class TutorSightTests(TestCase):
    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to TutorSight')
