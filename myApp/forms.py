from django.contrib.auth.forms import UserCreationForm
from .models import User,ContentCreator,Sponsor
from django import forms 


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','phone']

class UpdateBusinessProfile(forms.ModelForm):
    class Meta:
        model = ContentCreator
        fields = ['channelname','total_subscriber','description','about','contactinfo','contentstyle','image']
        