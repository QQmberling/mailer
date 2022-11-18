from django.db import models


class Message(models.Model):
    """
    Base class to inherit all further models from: adds default fields, such as created_at, updated_at, etc
    """
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    subject = models.CharField(null=True, blank=True, max_length=1024)
