from django.contrib import admin
from .models import Paste

admin.site.disable_action('delete_selected')

def enable_paste(modeladmin, request, queryset):
	queryset.update(status='enable')
enable_paste.short_description = "Mark pastes as enabled"

def disable_paste(modeladmin, request, queryset):
	queryset.update(status='diable')
disable_paste.short_description = "Mark pastes as disabled"

class PasteAdmin(admin.ModelAdmin):
	readonly_fields = ['privacy', 'title', 'author', 'date_posted', 'content', 'expiry', 'invited_users']
	def has_add_permission(self, request, obj=None):
		return False
	def has_delete_permission(self, request, obj=None):
		return False
	list_display = ['title', 'author', 'date_posted', 'status']
	ordering = ['title']
	actions = [enable_paste, disable_paste]

admin.site.register(Paste, PasteAdmin)
