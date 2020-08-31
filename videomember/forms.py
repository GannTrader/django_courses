from django import forms

class loginForm(forms.Form):
	username = forms.CharField(max_length = 255, widget = forms.TextInput(attrs = {
		'class': 'form-control',
		'placeholder': 'Enter Your Name',
		}))
	password = forms.CharField(max_length = 255, widget = forms.PasswordInput(attrs = {'class': 'form-control',
		'placeholder': 'Enter Your Pass',
		}))