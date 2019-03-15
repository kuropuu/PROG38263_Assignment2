from django.urls import path
from . import views
from .views import (
	PasteListView,
	UserPasteListView,
	PasteDetailView,
	PasteCreateView,
	PasteUpdateView,
	PasteDeleteView,
	search
)

urlpatterns = [
	path('', PasteListView.as_view(), name='home'),
	path('user/<str:username>', UserPasteListView.as_view(), name='user-pastes'),
	path('paste/new/', PasteCreateView.as_view(), name='paste-create'),
	path('paste/<str:slug>/', PasteDetailView.as_view(), name='paste-detail'),
	path('paste/<str:slug>/update/', PasteUpdateView.as_view(), name='paste-update'),
	path('paste/<str:slug>/delete/', PasteDeleteView.as_view(), name='paste-delete'),
	path('search/', search, name='search'),
]
