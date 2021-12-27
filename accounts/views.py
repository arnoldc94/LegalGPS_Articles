from accounts.models import CustomUser
from django.views.generic import  TemplateView
from django.views.generic.edit import CreateView
from accounts.forms import CustomUserCreationForm
from django.urls import reverse_lazy






class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

class ProfilePageView(TemplateView):
    template_name = "profile.html"









