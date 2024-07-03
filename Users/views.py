from email.message import EmailMessage
from random import randint

from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

from Users.forms import UserForm, CustomPasswordResetForm
from .forms import CustomSetPasswordForm


# from finalproject.settings import EMAIL_HOST_USER


class UserCreateView (CreateView):
    template_name = 'Users/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.first_name = new_user.first_name.title()
        new_user.last_name = new_user.last_name.title()

        # random_number = randint (1000, 9999)
        # new_user.username = f'{new_user.first_name[0].lower ()}{new_user.last_name[0].lower ().replace (" ", "")}_{random_number}'

        new_user.save()
        return super(UserCreateView, self).form_valid(form)
class CustomLogoutView (LogoutView):
    def dispatch(self, *args, **kwargs):
        logout(self.request)
        return redirect('login')

        # Trimitere mail cu tempalte
        # details_user = {
        #     'full_name': f'{new_user.first_name} {new_user.last_name}',
        #     'username': new_user.username,
        #
        # }
        # subject = 'Confirmare cont nou!'
        # message = get_template('mail.html').render(details_user)
        # mail = EmailMessage(subject, message, EMAIL_HOST_USER, [new_user.email])
        # mail.get_content_subtype = 'html'
        # mail.send()


class CustomPasswordResetView (PasswordResetView):
    template_name = 'registration/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

    form_class = CustomPasswordResetForm


class CustomPasswordResetConfirmView (PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

    form_class = CustomSetPasswordForm


class CustomPasswordResetDoneView (PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'


class CustomPasswordResetCompleteView (PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'
