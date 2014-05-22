from rest_framework import serializers

from backend.models import Tipo


class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ('id', 'nome', 'observacoes', 'ativo', 'excluido', 'data_hora_criacao',
                  'usuario_criacao', 'data_hora_atualizacao', 'usuario_atualizacao')