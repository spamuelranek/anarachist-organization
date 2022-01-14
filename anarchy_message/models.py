from django.contrib.auth import get_user_model
from django.db import models


GROUPS = (
  ('total anarchy', 'TOTAL ANARCHY'),
  ('empathatic anarchy','EMPATHATIC ANARCHY'),
  ('constrained anarchy', 'CONSTRAINED ANARCHY'),
  ('nihilist anarchy', 'NIHILIST ANARCHY')
)
GODS = (
  ('christian theological god', 'CHRISTIAN THEOLOGICAL GOD'),
  ('christian theological devil', 'CHRISTIAN THEOLOGICAL DEVIL'),
  ('satan', 'SATAN'),
  ('tiamat', 'TIAMAT'),
  ('cronus', 'CRONUS')
)
class Message(models.Model):
  title = models.CharField(max_length=48)
  group = models.CharField(max_length = 25, choices= GROUPS, default='total anarchy')
  message = models.TextField(max_length = 512, default='')
  statanic_god_supporter = models.CharField(max_length = 64, choices=GODS, default='satan' )
  poster = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)