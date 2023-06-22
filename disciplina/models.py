from django.db import models

class Disciplina(models.Model):
    codigo = models.IntegerField()
    nome = models.CharField(max_length=100)
    consultarDisciplina = models.BooleanField(default=False)
    incluirDisciplina = models.BooleanField(default=False)
