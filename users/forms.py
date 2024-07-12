from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

# user login form
# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=255)
#     password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Username",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
            }
        )
    )
    remember_me = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": "agree-term"})
    )


# User Registration Form
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm Password",
            }
        )
    )
    contact = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Contact",
            }
        )
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "email"]
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Username"}
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "First Name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
        }

    # check password matches
    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        return cd["password2"]


# Custom Password Change Form
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Old Password",
                "class": "form-control",
            }
        )
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "New Password",
                "class": "form-control",
            }
        ),
        help_text=(
            "Your password can’t be too similar to your other personal information.<br>"
            "Your password must contain at least 8 characters.<br>"
            "Your password can’t be a commonly used password.<br>"
            "Your password can’t be entirely numeric."
        ),
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm New Password",
                "class": "form-control",
            }
        )
    )
