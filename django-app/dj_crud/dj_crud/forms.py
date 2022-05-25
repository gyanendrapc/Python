from django import forms

class UserDetailsForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    concat =forms.CharField(label='Your contact',max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Your email',max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))