from django.db import models

class Video(models.Model):
    titulo = models.CharField(max_length=200)
    embed_url = models.URLField()  # URL para o vídeo embutido (ex: YouTube)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo
