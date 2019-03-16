from django.urls import path
from . import views
from .views import (
	PasteListView,
	UserPasteListView,
	PasteDetailView,
	PasteCreateView,
	PasteUpdateView,
	PasteDeleteView,
	search,
	UploadPasteView,
	UploadPasteDetailView,
	UploadPasteDeleteView,
	UploadPasteUpdateView,
	download_paste,
	download_upload_paste
)

urlpatterns = [
	
	path('', PasteListView.as_view(), name='home'),
	path('user/<str:username>', UserPasteListView.as_view(), name='user-pastes'),
	path('paste/new/', PasteCreateView.as_view(), name='paste-create'),
	path('paste/upload/', UploadPasteView.as_view(), name='upload_paste'),
	path('paste/upload/<str:slug>/', UploadPasteDetailView.as_view(), name='upload_detail'),
	path('paste/upload/<str:slug>/delete', UploadPasteDeleteView.as_view(), name='upload_delete'),
	path('paste/upload/<str:slug>/update', UploadPasteUpdateView.as_view(), name='upload_update'),
	path('paste/download/<str:slug>/', download_paste, name='download-paste'),
	path('paste/download/upload/<str:slug>/', download_upload_paste, name='download-upload-paste'),
	path('paste/<str:slug>/', PasteDetailView.as_view(), name='paste-detail'),
	path('paste/<str:slug>/update/', PasteUpdateView.as_view(), name='paste-update'),
	path('paste/<str:slug>/delete/', PasteDeleteView.as_view(), name='paste-delete'),
	path('search/', search, name='search'),
]
