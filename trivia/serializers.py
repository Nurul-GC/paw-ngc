from rest_framework import serializers
from trivia.models import Perguntas, Resposta

class RespostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resposta
        fields = ["resposta", "esta_correcta"]

class PerguntaSerializer(serializers.ModelSerializer):
    respostas = RespostaSerializer(many=True, read_only=True)

    class Meta:
        model = Perguntas
        fields = ["categoria", "pergunta", "respostas"]
