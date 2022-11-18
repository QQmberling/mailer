from django.contrib import admin

from mailer.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('to', 'subject')
    fields = ('to', 'subject', 'context', 'created_at',)
    readonly_fields = ('to', 'subject', 'context', 'created_at',)
