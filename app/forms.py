from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Booking


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    # first_name = forms.CharField(max_length=200)
    # last_name = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ["username","email","password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
        
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']  


# Create custom widget in your forms.py file.
class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Booking
        fields =['From','To','date','no_of_trips']