from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    registro = models.IntegerField
    consultarTurma = models.BooleanField(default=False)
    lancarNotaAluno = models.BooleanField(default=False)
    realizarFrequencia = models.BooleanField(default=False)