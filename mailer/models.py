from django.db import models


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    to = models.CharField(null=True, blank=True, max_length=1024)
    subject = models.CharField(null=True, blank=True, max_length=1024)
    context = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f'Message to: {self.to} with subject: {self.subject}. Passed data: {self.context}'
