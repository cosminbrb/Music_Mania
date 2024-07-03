from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User



class AuthentificationNewForm (AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super (AuthentificationNewForm, self).__init__ (*args, **kwargs)
        self.fields['username'].widget.attrs.update ({'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update ({'placeholder': 'Password'})


class UserForm (UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super (UserForm, self).__init__ (*args, **kwargs)
        self.fields['username'].widget.attrs.update ({'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update ({'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update ({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update ({'placeholder': 'Confirm Password'})


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email', max_length=254)


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'New Password'})
    )
    new_password2 = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm New Password'})
    )
