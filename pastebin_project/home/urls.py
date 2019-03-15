from django.urls import path
from . import views
from .views import (
	PasteListView,
	PasteDetailView,
	PasteCreateView,
	PasteUpdateView,
	PasteDeleteView,
	search,
	UploadPasteView,
	UploadPasteDetailView,
	UploadPasteDeleteView,
	UploadPasteUpdateView
)

urlpatterns = [
	
	path('', PasteListView.as_view(), name='home'),
	path('paste/<int:pk>/', PasteDetailView.as_view(), name='paste-detail'),
	path('paste/new/', PasteCreateView.as_view(), name='paste-create'),
	path('paste/<int:pk>/update/', PasteUpdateView.as_view(), name='paste-update'),
	path('paste/<int:pk>/delete/', PasteDeleteView.as_view(), name='paste-delete'),

	path('paste/upload/', UploadPasteView.as_view(), name='upload_paste'),
	path('paste/upload/<int:pk>/', UploadPasteDetailView.as_view(), name='upload_detail'),
	path('paste/upload/<int:pk>/delete', UploadPasteDeleteView.as_view(), name='upload_delete'),
	path('paste/upload/<int:pk>/update', UploadPasteUpdateView.as_view(), name='upload_update'),

	path('search/', search, name='search'),
]
