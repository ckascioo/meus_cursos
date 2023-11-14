from django.db import models
import random

class Curso(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)  # Usar AutoField para gerar IDs automáticos
    curso = models.CharField(max_length=100)
    finalizado = models.BooleanField(default=False)
    descrição = models.TextField(max_length=255)