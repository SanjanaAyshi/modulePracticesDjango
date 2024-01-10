
from django.urls import path
from .views import (CustomPasswordChangeView, UserBankAccountUpdateView, UserLoginView,
    UserRegistrationView)
from . import views
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', views.userLogout, name='logout'),
    # path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile' ),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change')
]