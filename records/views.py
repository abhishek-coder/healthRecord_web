from django.shortcuts import render, redirect
from records import forms

from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.tpl')


def doctor_login(request):
    if request.method == 'POST':
        form = forms.DoctorLoginForm(request.POST)
        if form.is_valid():
            context = {}
            context['user'] = form.cleaned_data['username']
            context['password'] = form.cleaned_data['password']

            return redirect('patient_connect')
    else:
        form = forms.DoctorLoginForm()

    return render(request, 'doctor_login.tpl', {'form': form})


def patient_connect(request):
    if request.method == 'POST':
        form = forms.PatientConnectForm(request.POST)
        if form.is_valid():
            aadhar_no = form.cleaned_data['aadhar_number']
            if aadhar_no:
                """ aadhar API authentication, this will provide patient_id """
                patient_id = 2

            return redirect('patient_detail', kwargs={'patient_id': patient_id})
    else:
        form = forms.PatientConnectForm()

    return render(request, 'aadharentry.html', {'form': form})


def patient_detail(request, patient_id):
    if request.method == 'POST':
        form = forms.ProfileDetailForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/done/')
    else:
        form = forms.ProfileDetailForm()

    return render(request, 'profile.html', {'form': form, 'patient_id': patient_id})
