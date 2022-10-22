from turtle import title
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1=User.objects.create_user(
            username='testuser2',password='1234'
        )
        testuser1.save()

        test_post=Post.objects.create(
            author=testuser1,title='BLog title test',body='Body content test...'
        )
        test_post.save()

    def test_blog_content(self):
        post=Post.objects.get(id=1)
        author=f'{post.author}'
        title=f'{post.title}'
        body=f'{post.body}'
        print
        self.assertEqual(author,'testuser2')
        self.assertEqual(title,'BLog title test')
        self.assertEqual(body,'Body content test...')
