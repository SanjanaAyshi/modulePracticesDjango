from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.register, name='register'),
    path('edit/<int:id>', views.edit_MU, name="edit_album"),
    path('login/', views.UserLoginView.as_view(), name='userLogin'),
    # path('profile/', views.profile, name='profile')

]
