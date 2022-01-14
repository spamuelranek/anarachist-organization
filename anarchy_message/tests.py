from email import message
from django.test import TestCase

from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Message

class MessageTests(TestCase):

  @classmethod
  def setUpTestData(cls):
      test_user = get_user_model().objects.create_user(username='tester',password='pass')
      test_user.save()

      test_message = Message.objects.create(
          poster = test_user,
          title = 'Title of Blog',
          message = 'Words about the blog',
          statanic_god_supporter = 'dog',
          group = 'Make'
      )
      test_message.save()

  def test_blog_content(self):
      message = Message.objects.get(id=1)
      

      self.assertEqual(str(message.poster), 'tester')
      self.assertEqual(message.title, 'Title of Blog')
      self.assertEqual(message.message, 'Words about the blog')
      self.assertEqual(message.statanic_god_supporter, 'dog')
      self.assertEqual(message.group, 'Make')
