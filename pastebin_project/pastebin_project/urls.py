"""pastebin_project URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
	 path('', include('home.urls')),
	 path('register/', user_views.register, name='register'),
	 path('profile/', user_views.profile, name='profile'),
	 path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
	 path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
	 path('password/', user_views.change_password, name='change-password'),
    path('delete/', user_views.delete_user, name='user-delete'),
    path('inbox/', include('notifications.urls')),
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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
