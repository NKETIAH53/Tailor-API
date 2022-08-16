from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ["email", "username", "first_name", "last_name", "role"]
        error_class = "error"


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name", "role"]
        error_class = "error"
