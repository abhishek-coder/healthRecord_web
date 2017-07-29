from django import forms


class PatientConnectForm(forms.Form):
    aadhar_number = forms.CharField(label='Aadhar Number', max_length=12)


class DoctorLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileDetailForm(forms.Form):
    age = forms.IntegerField()
    gender = forms.CharField(max_length=1)
    state = forms.CharField(max_length=30)
