from django.test import TestCase
from .models import Post, Comment, Tag


class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title="Hello", content="hello", status="ACTIVE",
                            image="alex-dukhanov-RHItvgIJfgw-unsplash.jpg", author="admin")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        post1 = Post.objects.get(title="Hello")
        self.assertEqual(post1.speak(), 'The lion says "roar"')

