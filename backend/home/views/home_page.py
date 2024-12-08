from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

@api_view(['GET'])
def home_page(request, format=None):
    return Response({
        'banners': reverse('banner-lista', request=request, format=format),
        'categorias': reverse('categoria-lista', request=request, format=format),
        'noticias': reverse('noticia-lista', request=request, format=format),
        'servicos': reverse('servico-lista', request=request, format=format),
        'videos': reverse('video-lista', request=request, format=format),
        'links_rapidos': reverse('linkrapido-lista', request=request, format=format),
    })
