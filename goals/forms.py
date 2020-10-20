from django import forms
from django.contrib.auth.models import User
from goals.models import Goals


class GoalsModelForm(forms.ModelForm):
    class Meta:
        model = Goals
        fields = ('title',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
