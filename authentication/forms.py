from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=66, label="Nom Utilisateur")
    password = forms.CharField(max_length=66, widget=forms.PasswordInput, label="Mot de passe")