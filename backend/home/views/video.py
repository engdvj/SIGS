from rest_framework import generics
from home.models.video import Video
from home.serializers.video import VideoSerializer

class VideoLista(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    name = 'Listagem de Vídeos'

class VideoDetalhe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    name = 'Detalhes do Vídeo'
