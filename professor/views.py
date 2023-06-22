from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import generics
from .models import Professor
from .serializers import ProfessorSerializer

class ProfessorViewSets(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
