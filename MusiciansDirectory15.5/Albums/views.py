from django.shortcuts import render, redirect
from . import forms
# Create your views here.
from . import models


def addAlbum(request):
    if request.method == 'POST':
        AlbumForm = forms.AlbumFrom(request.POST)
        if AlbumForm.is_valid():
            AlbumForm.save()
            return redirect('add_Album')

    else:
        AlbumForm = forms.AlbumFrom()
    return render(request, 'addAlbums.html', {'form':  AlbumForm})


def deleteAlbum(request, id):
    album = models.Album.objects.get(pk=id)
    album.delete()
    return redirect('homepage')
