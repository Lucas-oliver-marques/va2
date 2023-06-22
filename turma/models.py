from django.db import models

class Turma(models.Model):
    codigo = models.IntegerField
    listarTurma = models.BooleanField(default=False)
    listarAlunos = models.BooleanField(default=False)
