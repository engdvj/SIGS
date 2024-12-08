from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    icone = models.ImageField(upload_to='icones/', blank=True, null=True)

    def __str__(self):
        return self.nome
