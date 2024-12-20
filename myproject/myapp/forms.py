from django import forms
from .models import Stock, Farmer, Agronomist

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['seed', 'fertilizer', 'seedquantity', 'fertilizerquantity', 'planting_season']
        widgets = {
            'seed': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Seed Name'}),
            'fertilizer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Fertilizer Name'}),
            'seedquantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Seed Quantity'}),
            'fertilizerquantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Fertilizer Quantity'}),
            'planting_season': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Planting Season'}),
        }

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['firstname', 'lastname', 'contact', 'password', 'address']  # Removed 'created_at'
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name (Optional)'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Contact Number'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address (Optional)', 'rows': 3}),
        }

    def save(self, commit=True):
        farmer = super().save(commit=False)
        farmer.set_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            farmer.save()
        return farmer

from django import forms


class UserLoginForm(forms.Form):
    contact = forms.CharField(max_length=150, label='Name or Contact')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    from django import forms
from .models import Farmer

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['firstname', 'lastname', 'contact']  # Add other relevant fields as needed
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
        }


        from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']  # Include other fields as necessary

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

        widgets = {
            'old_password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}),
            'new_password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'}),
            'new_password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm New Password'}),
        }