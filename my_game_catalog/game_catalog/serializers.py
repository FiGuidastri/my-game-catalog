# serializers.py
from rest_framework import serializers
from .models import Jogo

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__'  # Ou especifique os campos que você precisa
