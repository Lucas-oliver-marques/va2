from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import generics
from .models import Aluno
from .serializers import AlunoSerializer

class AlunoViewSets(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
