from django.contrib.auth.forms import UserCreationForm,AuthenticationForm 
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput,TextInput 
 #create
class userCreationForm(UserCreationForm):

    class Meta:

         model = User
         fields = ['username','email']








