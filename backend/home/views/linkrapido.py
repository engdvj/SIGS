from rest_framework import generics
from home.models.linkrapido import LinkRapido
from home.serializers.linkrapido import LinkRapidoSerializer

class LinkRapidoLista(generics.ListCreateAPIView):
    queryset = LinkRapido.objects.all()
    serializer_class = LinkRapidoSerializer
    name = 'Listagem de Links Rápidos'

class LinkRapidoDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = LinkRapido.objects.all()
    serializer_class = LinkRapidoSerializer
    name = 'Detalhes do Link Rápido'
