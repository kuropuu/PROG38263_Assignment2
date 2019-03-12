from django.urls import path
from . import views
from .views import (
	PasteListView,
	PasteDetailView,
	PasteCreateView,
	PasteUpdateView,
	PasteDeleteView,
	search
)

urlpatterns = [
	path('', PasteListView.as_view(), name='home'),
	path('paste/<int:pk>/', PasteDetailView.as_view(), name='paste-detail'),
	path('paste/new/', PasteCreateView.as_view(), name='paste-create'),
	path('paste/<int:pk>/update/', PasteUpdateView.as_view(), name='paste-update'),
	path('paste/<int:pk>/delete/', PasteDeleteView.as_view(), name='paste-delete'),
	path('search/', search, name='search'),
]
