from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, Textarea

class NewUserForm(UserCreationForm):

    # widgets = { 'address': forms.TextInput(attrs={'size': 20})}

    email = forms.EmailField(required=True)
    library_card_number = forms.IntegerField(required=True)
    address_line_1 = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    postal_code = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "library_card_number", "address_line_1", "city", "state", "postal_code", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.library_card = self.cleaned_data['library_card_number']
        if commit:
            user.save()
        return user


