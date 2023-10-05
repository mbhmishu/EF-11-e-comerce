from django.forms import ModelForm
from AccountApp.models import User, UserProfile
from django.contrib.auth.forms import UserCreationForm

#forms 

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

