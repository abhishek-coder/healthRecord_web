from django.contrib.auth import authenticate, login


def login_doctor(request, username, password):
    user = authenticate(username=username, password=password)
    if user and hasattr(user, 'doctor'):
        login(request, user)
        return True
    else:
        return False
