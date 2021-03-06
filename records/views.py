from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from records import forms
from records import models
from django.http import HttpResponseRedirect, HttpResponse, Http404


from . import auth, forms, models


def index(request):
    # If user is logged-in and user is a doctor, redirect to home page
    if request.user.is_authenticated() and hasattr(request.user, 'doctor'):
        return redirect('patient_connect')
    return render(request, 'index.tpl')


def doctor_login(request):
    # If user is logged-in and user is a doctor, redirect to home page
    if request.user.is_authenticated() and hasattr(request.user, 'doctor'):
        return redirect('patient_connect')

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
                return redirect('patient_detail', patient_id=patient.id)
        return render(request, 'patient_connect.tpl', {'form': form, 'error': True})

    else:
        form = forms.PatientConnectForm()

    return render(request, 'patient_connect.tpl', {'form': form})


@login_required
def patient_detail(request, patient_id):
    patient = models.Patient.objects.get(id=patient_id)

    return render(request, 'patient_detail.tpl', {
        'patient': patient,
        'aadhar_data': patient.user.useraadhar
    })


@login_required
def history(request, patient_id):
    patient = models.Patient.objects.get(id=int(patient_id))
    patient_name = patient.user.get_full_name()
    aadhar_data = patient.user.useraadhar

    return render(request, 'patient_history.tpl', {
        'patient': patient,
        'aadhar_data': patient.user.useraadhar,
        'cases': patient.cases.all()
    })


@login_required
def case_detail(request, patient_id, case_id):
    patient = models.Patient.objects.get(id=int(patient_id))
    case = patient.cases.get(id=case_id)
    aadhar_data = patient.user.useraadhar

    return render(request, 'case_detail.tpl', {
        'patient': patient,
        'aadhar_data': patient.user.useraadhar,
        'case': case
    })


@login_required
def new_case(request, patient_id):
    patient = models.Patient.objects.get(id=int(patient_id))
    if request.method == 'POST':
        form = forms.NewCaseForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            notes = form.cleaned_data['notes']
            symptoms = form.cleaned_data['notes']
            prescription = form.cleaned_data['prescription']
            document_doc = form.cleaned_data['document']

            try:
                doctor = request.user.doctor
            except:
                 raise Http404()
            try:
                patient = models.Patient.objects.get(id=int(patient_id))
            except models.Patient.DoesNotExist:
                raise Http404
            # Create Entry for a new case
            case = models.Case.objects.create(
                patient=patient, doctor=doctor, title=title, notes=notes)
            document = models.Document.objects.create(
                text=prescription, upload=document_doc)
            models.Record.objects.create(
                case=case, prescription=document, symptoms=symptoms)
            return redirect('case_detail', patient_id=patient_id, case_id=case.id)

    # Return template if get request
    return render(request, 'new_case.tpl', {'patient':patient})
