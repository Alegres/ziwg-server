from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation

class SignUpForm(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class EmailChangeForm(forms.Form):

    error_messages = {
        'email_mismatch': _("The two email addresses fields didn't match."),
        'not_changed': _("The email address is the same as the one already defined."),
    }

    new_email1 = forms.EmailField(
        label=_("New e-mail"),
        widget=forms.EmailInput,
    )

    new_email2 = forms.EmailField(
        label=_("Repeat new e-mail"),
        widget=forms.EmailInput,
    )
class CustomPasswordChangeForm(PasswordChangeForm):
     fields = ('old_password',  'new_password1', 'new_password2')
    
