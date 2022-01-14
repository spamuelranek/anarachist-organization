from django.urls import path
from .views import MessageDetailView, MessageListView


urlpatterns = [
  path("",MessageListView.as_view(), name = "message_list"),
  path("<int:pk>/",MessageDetailView.as_view(), name = "message_detail"),
]