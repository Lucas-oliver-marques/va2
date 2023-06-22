from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import generics
from .models import Curso
from .serializers import CursoSerializer

class CursoViewSets(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
