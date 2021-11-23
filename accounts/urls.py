from django.urls import path
from .views import SignUpView
from simple_chatbot.views import SimpleChatbot

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path("simple_chatbot/", SimpleChatbot.as_view()),
]



