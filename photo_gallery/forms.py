from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove all default help text (password requirements, username hints)
        for field in self.fields.values():
            field.help_text = None
            field.widget.attrs.update({
                'class': 'w-full p-2 border border-darkBrown/20 rounded-md bg-warmCream focus:outline-none focus:border-sageGreen'
            })