from django.contrib import admin
from django.urls import path, include
from home.views.home_page import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('home.urls')),  # Inclui as rotas da API
    path('', home_page, name='api-root'),  # Página inicial da API navegável
]
