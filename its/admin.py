from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from its.models import IssueType, IssuePriority, Issue


@admin.register(IssueType)
class IssueTypeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    list_per_page = 10


@admin.register(IssuePriority)
class IssuePriorityAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    list_per_page = 10


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'get_created_by_title',
        'get_issue_type',
        'get_issue_priority',
        'get_issue_status',
        'get_assigned_to',
        'add_date',
        'end_date',
    )
    list_per_page = 10
    list_filter = ('assigned_to', 'type', 'priority', 'status')
    actions = ['make_status_open']

    def make_status_open(self, request, queryset):
        queryset.update(status='Open')

    def get_created_by_title(self, obj):
        if obj.author.first_name and obj.author.last_name:
            return obj.author.first_name + ' ' + obj.author.last_name
        else:
            return obj.author.username

    def get_issue_priority(self, obj):
        return obj.priority.title

    def get_issue_status(self, obj):
        if obj.status.lower() == 'open':
            return format_html('<span class="badge badge-open">{}</span>', obj.status)
        elif obj.status.lower() == 'reopen':
            return format_html('<span class="badge badge-primary">{}</span>', obj.status)
        elif obj.status.lower() == 'in progress':
            return format_html('<span class="badge badge-warning">{}</span>', obj.status)
        elif obj.status.lower() == 'fixed':
            return format_html('<span class="badge badge-success">{}</span>', obj.status)
        elif obj.status.lower() == 'closed':
            return format_html('<span class="badge badge-dark">{}</span>', obj.status)

    def get_issue_type(self, obj):
        return obj.type.title

    def get_assigned_to(self, obj):
        if obj.author.first_name and obj.author.last_name:
            return obj.author.first_name + ' ' + obj.author.last_name
        else:
            return obj.author.username

    make_status_open.short_description = _('Mark selected issues as opened')
    get_created_by_title.short_description = _('Created By')
    get_issue_priority.short_description = _('Priority')
    get_issue_status.short_description = _('Status')
    get_issue_type.short_description = _('Type')
    get_assigned_to.short_description = _('Assigned To')

    class Media:
        css = {
            'all': ('css/admin/issue_admin.css',)
        }




