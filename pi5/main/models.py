from django.db import models
from django.contrib.auth.models import User

class Tipo(models.Model):
    tipo = models.CharField(max_length=30)
    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
    def __str__(self):
        return self.tipo