from django import forms

from apps.tree.models import PlantedTree


class PlantedTreeModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user is not None:
            self.fields['account'].queryset = user.extension.account.all()

    class Meta:
        model = PlantedTree
        exclude = ['user', 'planted_at']
        widgets = {
            "age": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Idade da árvore"}),
            "location_latitude": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Latitude"}),
            "location_longitude": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Longitude"}),
            "tree": forms.Select(attrs={"class": "form-control select2bs4 tree"}),
            "account": forms.Select(attrs={"class": "form-control select2bs4 account"}),
        }
