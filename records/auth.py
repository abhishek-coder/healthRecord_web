from django.contrib.auth import authenticate, login

from . import models


def login_doctor(request, username, password):
    user = authenticate(username=username, password=password)
    if user and hasattr(user, 'doctor'):
        login(request, user)
        return True
    else:
        return False


def authenticate_patient_with_aadhar(doctor, aadhar):
    """TODO: Linking with aadhar API"""
    try:
        patient = models.Patient.objects.get(user__useraadhar__number=aadhar)
        return patient
    except models.Patient.DoesNotExist:
        return False
