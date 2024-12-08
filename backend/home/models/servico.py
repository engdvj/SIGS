from django.db import models
from .categoria import Categoria  # Importa Categoria para relacionamento

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    url = models.URLField()  # Link para o serviço
    icone = models.ImageField(upload_to='icones/', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='servicos')
    dispositivos_disponiveis = models.CharField(
        max_length=50, 
        choices=[('desktop', 'Desktop'), ('mobile', 'Mobile'), ('both', 'Both')], 
        default='both'
    )

    def __str__(self):
        return self.nome
