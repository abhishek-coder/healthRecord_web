from django import forms


class AaddharEntryForm(forms.Form):
    aadhar_number = forms.CharField(label='Aadhar Number', max_length=16)


class Login(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.Form):
    image = forms.ImageField()
    age = forms.IntegerField()
    sex = forms.CharField(max_length=1)
    state = forms.CharField(max_length=30)



