from backend.serializers import PontoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.models import Registro


class PontoView(APIView):
    def get(self, request, format=None):
        pontos = Registro.objects.all()
        serializer = PontoSerializer(pontos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PontoSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
