from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(widget = forms.TextInput(attrs = {"class": "form-control", "id": "form_full_name",
                                                                 "placeholder": "Full Name"}))
    email = forms.EmailField(widget = forms.EmailInput(attrs = {"class": "form-control", "id": "email",
                                                                 "placeholder": "Email"}))
    content = forms.CharField(widget = forms.Textarea(attrs = {"class": "form-control", "id": "message",
                                                                 "placeholder": "Message"}))


    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "gmail.com" not in email:
            raise forms.ValidationError("Email has to be Gmail.com")
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput(attrs = {}))


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(widget = forms.EmailInput(attrs = {"class": "form-control", "id": "email",
                                                                 "placeholder": "Email"}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {}))
    password2 = forms.CharField(label = 'Confirm Password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username Already Exists!")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email Already Exists!")


    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise forms.ValidationError("Password must match.")
        return data