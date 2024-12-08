from rest_framework import generics
from home.models.banner import Banner
from home.serializers.banner import BannerSerializer

class BannerLista(generics.ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    name = 'Listagem de Banners'

class BannerDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    name = 'Detalhes do Banner'
