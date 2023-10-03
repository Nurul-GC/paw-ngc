from django.db import models

class Perguntas(models.Model):
    categoria = models.CharField(max_length=50)
    pergunta = models.TextField()

class Resposta(models.Model):
    pergunta = models.ForeignKey(Perguntas, on_delete=models.CASCADE, related_query_name="question")
    resposta = models.TextField()
    esta_correcta = models.BooleanField()

    def __str__(self):
        return self.resposta
