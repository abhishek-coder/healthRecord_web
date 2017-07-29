from django.shortcuts import render
from records.forms import AaddharEntryForm, Login, ProfileForm

from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.tpl')


def aadharentryview(request):
    if request.method == 'POST':
        form = AaddharEntryForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = AaddharEntryForm()

    return render(request, 'aadharentry.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            context = {}
            context['user'] = form.cleaned_data['username']
            context['password'] = form.cleaned_data['password']

            return render(request, 'login.html', context)
    else:
        form = Login()

    return render(request, 'login.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/done/')
    else:
        form = ProfileForm()

    return render(request, 'profile.html', {'form': form})
