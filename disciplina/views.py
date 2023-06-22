from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import generics
from .models import Disciplina
from .serializers import DisciplinaSerializer

class DisciplinaViewSets(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
