from rest_framework import generics
from home.models.noticia import Noticia
from home.serializers.noticia import NoticiaSerializer

class NoticiaLista(generics.ListCreateAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer
    name = 'Listagem de Notícias'

class NoticiaDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer
    name = 'Detalhes da Notícia'
