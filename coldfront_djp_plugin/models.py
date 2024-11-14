from django.db import models

class DummyModel(models.Model):
    """Included to demonstrate model is detected by Django."""
    name = models.CharField(max_length=100)
