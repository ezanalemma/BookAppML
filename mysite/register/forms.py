from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    library_card_number = forms.IntegerField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "library_card_number", "password1", "password2",)

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.library_card = self.cleaned_data['library_card']
        if commit:
            user.save()
        return user


