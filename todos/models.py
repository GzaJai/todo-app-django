from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Todo(models.Model):

    STATUS_CHOICE = [
        ("P", "Pendiente"),
        ("H", "En progreso"),
        ("D", "Finalizada"),
    ]

    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default="P")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
