from django.shortcuts import render
from rest_framework import viewsets
from trivia.models import Perguntas
from trivia.serializers import PerguntaSerializer


class PerguntaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Perguntas.objects.all()
    serializer_class = PerguntaSerializer
