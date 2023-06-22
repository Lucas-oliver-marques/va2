"""
URL configuration for va2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework import viewsets
from aluno.views import AlunoViewSets
from curso.views import CursoViewSets
from disciplina.views import DisciplinaViewSets
from professor.views import ProfessorViewSets
from turma.views import TurmaViewSets

rotas = routers.DefaultRouter()
rotas.register(r'aluno', AlunoViewSets, basename='Aluno'),
rotas.register(r'curso', CursoViewSets, basename='Curso'),
rotas.register(r'disciplina', DisciplinaViewSets, basename='Disciplina'),
rotas.register(r'professor', ProfessorViewSets, basename='Professor'),
rotas.register(r'turma', TurmaViewSets, basename='Turma'),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rotas.urls)),
]
