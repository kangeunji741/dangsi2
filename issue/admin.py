from django.contrib import admin

from issue.models import Issue


class IssueAdmin(admin.ModelAdmin):
    list_display = ['id', 'issue_title']


admin.site.register(Issue, IssueAdmin)