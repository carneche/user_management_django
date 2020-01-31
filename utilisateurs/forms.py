from django import forms

class ConnexionForm(forms.Form):
    identifiant = forms.CharField(max_length=30)
    mot_de_passe = forms.CharField(max_length=30)