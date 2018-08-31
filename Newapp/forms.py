from django import forms
from Newapp.models import Register


class RegisterForm(forms.ModelForm):
    class Meta():
        model=Register
        fields=('Name','Email','Roll','Branch')
        widgets = {
            'Name': forms.TextInput({'placeholder': 'Enter Name'}),
            'Email': forms.TextInput({'placeholder': 'Enter Email'}),
            'Roll': forms.TextInput({'placeholder': 'Enter Roll No'}),
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['Name'].label = 'NAME'
        self.fields['Email'].label = 'EMAIL'
        self.fields['Roll'].label = 'ROLL NO'
        self.fields['Branch'].label = 'BRANCH'