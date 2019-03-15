from django.urls import path, include
from .views import (
		NotificationsView,
		show_notification,
		delete_notification,
		AddKeywordView
	)

urlpatterns = [
	path('inbox/', NotificationsView.as_view(), name="inbox"),
	path('inbox/show/<int:pk>/', show_notification, name="show_notification"),
	path('inbox/delete/<int:pk>/', delete_notification, name="delete_notification"),
	path('inbox/add/', AddKeywordView.as_view(), name="add_keyword")
]
