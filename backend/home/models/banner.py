from django.db import models

class Banner(models.Model):
    titulo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='banners/')
    link = models.URLField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo
