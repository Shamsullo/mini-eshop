from django.forms import ModelForm
from .models import MyUser, UserProfile

from django.contrib.auth.forms import UserCreationForm
from django import forms

class CreateUserForm(UserCreationForm):

	class Meta:
		model = MyUser
		fields = ['first_name', 'username', 'email', 'phone_number', 'password1', 'password2']


class UpdateUserProfileForm(forms.ModelForm):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	email  = forms.EmailField(max_length=100)
	phone_number = forms.CharField(max_length=100)
	class Meta:
		model = UserProfile
		fields = ['first_name', 'last_name', 'email', 'phone_number', 'location', 'bio']
