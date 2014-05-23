from rest_framework import serializers

from backend.models import Ponto


class PontoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ponto
        fields = ('id', 'valor', 'periodo', 'conta', 'observacoes', 'ativo', 'excluido', 'data_hora_criacao',
                  'usuario_criacao', 'data_hora_atualizacao', 'usuario_atualizacao')