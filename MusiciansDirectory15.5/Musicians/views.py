from django.shortcuts import render, redirect
from . import forms
# Create your views here.
from . import models


def addMusician(request):
    if request.method == 'POST':
        musiciansForm = forms.MusiciansFrom(request.POST)
        if musiciansForm.is_valid():
            musiciansForm.save()
            return redirect('add_Musician')

    else:
        musiciansForm = forms.MusiciansFrom()
    return render(request, 'addMusicians.html', {'form':  musiciansForm})


def edit_MU(request, id):
    musician = models.Musicians.objects.get(pk=id)
    musiciansForm = forms.MusiciansFrom(instance=musician)
    if request.method == 'POST':
        musiciansForm = forms.MusiciansFrom(request.POST, instance=musician)
        if musiciansForm.is_valid():
            musiciansForm.save()
            return redirect('homepage')

    return render(request, 'addMusicians.html', {'form': musiciansForm})
