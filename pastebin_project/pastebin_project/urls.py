"""pastebin_project URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from notifier import views as inbox_views

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include('home.urls')),
     path('register/', user_views.register, name='register'),
     path('profile/', user_views.profile, name='profile'),
     path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
     path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
     path('inbox/', inbox_views.inbox, name='inbox'),
     path('change_notifications/', user_views.change_notifications, name='change_notifications'),
     path('password_reset/', 
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), 
        name='password_reset'),
     path('password_reset_done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'),
     path('password_reset_confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
     path('password_reset_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),
     path('password/', user_views.change_password, name='change_password'),
]
