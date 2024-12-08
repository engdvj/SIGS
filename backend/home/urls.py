from django.urls import path
from .views import (
    BannerLista, BannerDetalhe,
    CategoriaLista, CategoriaDetalhe,
    LinkRapidoLista, LinkRapidoDetalhe,
    NoticiaLista, NoticiaDetalhe,
    ServicoLista, ServicoDetalhe,
    VideoLista, VideoDetalhe,
)

urlpatterns = [
    path('banners/', BannerLista.as_view(), name='banner-lista'),
    path('banners/<int:pk>/', BannerDetalhe.as_view(), name='banner-detalhe'),
    path('categorias/', CategoriaLista.as_view(), name='categoria-lista'),
    path('categorias/<int:pk>/', CategoriaDetalhe.as_view(), name='categoria-detalhe'),
    path('noticias/', NoticiaLista.as_view(), name='noticia-lista'),
    path('noticias/<int:pk>/', NoticiaDetalhe.as_view(), name='noticia-detalhe'),
    path('servicos/', ServicoLista.as_view(), name='servico-lista'),
    path('servicos/<int:pk>/', ServicoDetalhe.as_view(), name='servico-detalhe'),
    path('videos/', VideoLista.as_view(), name='video-lista'),
    path('videos/<int:pk>/', VideoDetalhe.as_view(), name='video-detalhe'),
    path('links-rapidos/', LinkRapidoLista.as_view(), name='linkrapido-lista'),
    path('links-rapidos/<int:pk>/', LinkRapidoDetalhe.as_view(), name='linkrapido-detalhe'),
]
