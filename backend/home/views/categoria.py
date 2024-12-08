from rest_framework import generics
from home.models.categoria import Categoria
from home.serializers.categoria import CategoriaSerializer

class CategoriaLista(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = 'Listagem de Categorias'

class CategoriaDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = 'Detalhes da Categoria'
