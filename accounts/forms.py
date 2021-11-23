
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'role', 'age', 'profile_pic' )

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields