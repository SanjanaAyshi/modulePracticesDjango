from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addAlbum, name='add_Album'),
    path('delete/<int:id>', views.deleteAlbum, name="delete_album"),
    # path('edit/<int:id>', views.edit_Album, name="edit_album"),
]
