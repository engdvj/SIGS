from rest_framework import generics
from home.models.servico import Servico
from home.serializers.servico import ServicoSerializer

class ServicoLista(generics.ListCreateAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    name = 'Listagem de Serviços'

class ServicoDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    name = 'Detalhes do Serviço'
