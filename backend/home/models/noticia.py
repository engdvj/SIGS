from django.db import models
from .categoria import Categoria  # Importa Categoria para relacionamento

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Categoria)  # Relacionamento com Categoria

    def __str__(self):
        return self.titulo
