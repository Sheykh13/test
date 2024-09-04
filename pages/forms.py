from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm
class updateuser_form(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','username']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','username',  'password1', 'password2']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

        
#nn
class updatepasswordform(SetPasswordForm):
    class meta:
        model=User
        fields=['new_password1','new_password2']


