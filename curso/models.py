from django.db import models

class Curso(models.Model):
    codigo = models.IntegerField()
    nome = models.CharField(max_length=100)
    consultarCurso = models.BooleanField(default=False)
    incluirCurso = models.BooleanField(default=False)
