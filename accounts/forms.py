from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class RegisterForm(UserCreationForm):

    email = forms.EmailField()

    first_name = forms.CharField(
        max_length=100
    )

    last_name = forms.CharField(
        max_length=100,
        required=False
    )

    phone = forms.CharField(
        max_length=30,
        required=False
    )

    class Meta:

        model = User

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'password1',
            'password2'
        ]

    def save(self, commit=True):

        user = super().save(commit=False)

        user.email = self.cleaned_data['email']

        user.first_name = self.cleaned_data['first_name']

        user.last_name = self.cleaned_data['last_name']

        if commit:

            user.save()

            Profile.objects.create(
                user=user,
                phone=self.cleaned_data['phone']
            )

        return user