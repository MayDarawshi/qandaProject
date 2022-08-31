from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput,PasswordInput


from django import forms



class UsersForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    # username=forms.CharField(widget=forms.TextInput(attrs={ 'style': 'width: 300px;', 'class': 'form-control'}))
    # email=forms.EmailField(widget=forms.EmailInput(attrs={  'style': 'width: 300px;', 'class': 'form-control'}))
    grade=forms.CharField(widget=forms.TextInput(attrs={ 'style': 'width: 300px;', 'class': 'form-control'}))
    phone=forms.CharField(widget=forms.TextInput(attrs={ 'style': 'width: 300px;', 'class': 'form-control'}))
    # password=forms.CharField(widget=forms.PasswordInput(attrs={ 'style': 'width: 300px;', 'class': 'form-control'}))
    school=forms.CharField(widget=forms.TextInput(attrs={ 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','grade','phone','school','password1','password2']
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),
            
            'grade':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                }),

            'password1':PasswordInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                }),
            'password2':PasswordInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                }),                     
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                }),
            'phone': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                }),
                'school': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                }),
            
        }
                


