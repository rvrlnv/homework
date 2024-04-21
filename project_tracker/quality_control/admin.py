from django.contrib import admin
from .models import BugReport, FeatureRequest

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'created_at')
    list_filter = ('project', 'status')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'project', 'task', 'status')
        }),
        ('Additional Info', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
    actions = ['change_bug_status']

    def change_bug_status(self, request, queryset):
        queryset.update(status='resolved')
    change_bug_status.short_description = "Mark selected bugs as resolved"

@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at')
    list_filter = ('project', 'status', 'priority')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'project', 'task', 'status', 'priority')
        }),
        ('Additional Info', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')