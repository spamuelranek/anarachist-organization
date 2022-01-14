from django.forms import fields
from rest_framework import serializers

from anarchy_message.models import Message

class MessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Message
    fields = ('title', 'group', 'message', 'statanic_god_supporter', 'poster')