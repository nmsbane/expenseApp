from django import forms
from django.contrib.auth.models import User
from .models import Account

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
    
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords are not matching')
        return cd['password2']
        
        
class AddAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'description', 'balance']


class AddBalanceForm(forms.Form):
    # here we use a dummy `queryset`, because ModelChoiceField
    # requires some queryset
    account_field = forms.ModelChoiceField(queryset=User.objects.none())
    amount = forms.IntegerField()

    def __init__(self, user):
        super(AddBalanceForm, self).__init__()
        self.fields['account_field'].queryset = user.accounts.all()
    