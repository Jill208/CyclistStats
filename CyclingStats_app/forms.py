from django import forms
from CyclingStats_app.models import Event, Cyclist


class Eventforms(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

class Cyclistforms(forms.ModelForm):
    class Meta:
        model=Cyclist
        fields="__all__"