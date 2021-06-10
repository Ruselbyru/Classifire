from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',register_page,name='register'),
    path('login/',login_page,name='login'),
    path('logout/',logout_page,name='logout'),
    path('user/',user_page,name='user'),
    path('update/',update_profile,name='update'),
    path('forgot/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('reset_done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset_confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_complite/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]