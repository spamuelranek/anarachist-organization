from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Message
from .serialization import MessageSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework import permissions

class MessageListView(ListCreateAPIView):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  queryset = Message.objects.all()
  serializer_class = MessageSerializer

class MessageDetailView(RetrieveUpdateDestroyAPIView):
  permission_classes = [IsAuthorOrReadOnly]
  queryset = Message.objects.all()
  serializer_class = MessageSerializer