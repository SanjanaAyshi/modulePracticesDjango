from django.shortcuts import render, redirect
from Albums.models import Album
# from .forms import AuthorForm


def home(request):
    data = Album.objects.all()
    return render(request, 'home.html', {'data': data})
