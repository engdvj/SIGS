from rest_framework import serializers
from home.models.linkrapido import LinkRapido

class LinkRapidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkRapido
        fields = '__all__'
