from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm

class CustomRegisterForm(UserCreationForm):
    photo = forms.ImageField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=100, required=True, initial='+996')
    adress = forms.CharField(max_length=200, initial='Bishkek')
    gender = forms.CharField(max_length=100, required=True, initial='m')
    status = forms.CharField(max_length=100, required=True, initial='married')
    kids = forms.CharField(max_length=100, required=True, initial='none')
    position = forms.CharField(max_length=100)
    salary = forms.IntegerField(label='Ожидаемая зарплата?')
    language = forms.CharField(max_length=100, initial='ru')

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'password1',
            'password2',
            'photo',
            'first_name',
            'email',
            'phone_number',
            'gender',
            'status',
            'kids',
            'position',
            'salary',
            'language'
        )



def save(self, commit = True):
    user = super(CustomRegisterForm, self).save(commit=False)
    user.email = self.cleaned_data['email']
    if commit:
        user.save()
    return user