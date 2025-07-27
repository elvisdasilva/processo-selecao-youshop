from django import forms
from apps.user.models import UserExtension


class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = UserExtension
        exclude = ["user", "account", "last_login", "date_joined"]
        widgets = {
            "bio": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Bio", "rows": 3}
            ),
        }
