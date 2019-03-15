from django.contrib import admin
from .models import Paste
from .models import UploadPaste

admin.site.disable_action('delete_selected')

def enable_paste(modeladmin, request, queryset):
	queryset.update(status='Enable')
enable_paste.short_description = "Mark pastes as enabled"

def disable_paste(modeladmin, request, queryset):
	queryset.update(status='Disable')
disable_paste.short_description = "Mark pastes as disabled"

class PasteAdmin(admin.ModelAdmin):
	readonly_fields = ['slug', 'privacy', 'title', 'author', 'date_posted', 'content', 'expiry', 'invited_users', 'expired']
	def has_add_permission(self, request, obj=None):
		return False
	def has_delete_permission(self, request, obj=None):
		return False
	list_display = ['title', 'author', 'date_posted', 'status']
	ordering = ['title']
	actions = [enable_paste, disable_paste]

class UploadPasteAdmin(admin.ModelAdmin):
	readonly_fields = ['slug', 'privacy', 'title', 'creator', 'date_posted', 'content', 'expiry', 'invited_users', 'expired']
	def has_add_permission(self, request, obj=None):
		return False
	def has_delete_permission(self, request, obj=None):
		return False
	list_display = ['title', 'creator', 'date_posted', 'status']
	ordering = ['title']
	actions = [enable_paste, disable_paste]

admin.site.register(Paste, PasteAdmin)
admin.site.register(UploadPaste, UploadPasteAdmin)
