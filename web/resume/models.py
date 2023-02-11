"""Models file for storing model for Resume"""
from uuid import uuid4

from django.db import models


class Resume(models.Model):
    """Model for storing and retrieving resume"""
    id = models.AutoField(primary_key=True)
    hash = models.UUIDField(default=uuid4)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id}"
