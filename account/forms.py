# from django.contrib.auth.forms import AuthenticationForm

# class LoginForm(AuthenticationForm):
#     """ログインフォーム"""
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs["class"] = "form-control"


from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    """ログインフォーム"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
        # 必要に応じて、'email', 'first_name', 'last_name' など他のフィールドを追加可能
