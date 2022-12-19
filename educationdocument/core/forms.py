from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['first_name', 'last_name','father_name','birthday','gender','point1','point2','fin']
      
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            new_class ={
                'class': 'form-control py-3',
                'placeholder': f'Enter your {self.fields[str(field)].label}'
            }
            self.fields[str(field)].widget.attrs.update(
                new_class
            )