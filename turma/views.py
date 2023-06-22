from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import generics
from .models import Turma
from .serializers import TurmaSerializer

class TurmaViewSets(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
