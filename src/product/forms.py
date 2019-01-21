from django import forms

from .models import User

class UserForm(forms.ModelForm):
        class Meta:
                model = User
                fields = [
                        'name',
                        'family',
                        'email',
                        'phoneNumber'
                ]


class RawUserForm(forms.Form):
        # userid = forms.CharField(label='شناسه مشتری')
        name = forms.CharField(label='نام')
        family = forms.CharField(label='نام خانوادگی')
        ssn = forms.DecimalField(label='شماره ملی')
        email = forms.CharField(label='پست الکترونیکی')
        phoneNumber = forms.DecimalField(label='شماره تلفن همراه')
        iban = forms.CharField(label='شماره شِبا')