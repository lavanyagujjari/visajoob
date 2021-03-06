from django import forms
from tutorial.models import UserProfileInfo,data_form
#from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = UserProfileInfo
        fields = ('username','password','email','mobileno')
	
#class UserProfileInfoForm(forms.ModelForm):
#     class Meta():
#         model = UserProfileInfo
#         fields = ('portfolio_site','profile_pic')

class DataForm(forms.ModelForm):
    class Meta():
        model = data_form
        fields = ('name','Mobile','area')