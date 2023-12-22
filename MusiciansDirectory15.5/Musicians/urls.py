from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addMusician, name='add_Musician'),
    path('edit/<int:id>', views.edit_MU, name="edit_album"),
]
