from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from . import auth, forms, models


def index(request):
    return render(request, 'index.tpl')


def doctor_login(request):
    if request.method == 'POST':
        form = forms.DoctorLoginForm(request.POST)
        if form.is_valid():
            logged_in = auth.login_doctor(
                request, form.cleaned_data['username'],
                form.cleaned_data['password'])
            if logged_in:
                return redirect('patient_connect')
        return render(request, 'doctor_login.tpl', {
            'form': form, 'error': True
        })
    else:
        form = forms.DoctorLoginForm()

    return render(request, 'doctor_login.tpl', {'form': form})


@login_required
def patient_connect(request):
    if request.method == 'POST':
        form = forms.PatientConnectForm(request.POST)
        if form.is_valid():
            aadhar_no = form.cleaned_data['aadhar_number']
            patient = auth.authenticate_patient_with_aadhar(
                request.user.doctor, aadhar_no)
            if patient:
                return redirect('patient_detail', kwargs={'patient_id': patient.id})
        return render(request, 'aadharentry.html', {'form': form, 'error': True})
    else:
        form = forms.PatientConnectForm()

    return render(request, 'aadharentry.html', {'form': form})


@login_required
def patient_detail(request, patient_id):
    if request.method == 'POST':
        form = forms.ProfileDetailForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/done/')
    else:
        form = forms.ProfileDetailForm()

    return render(request, 'profile.html', {'form': form, 'patient_id': patient_id})
