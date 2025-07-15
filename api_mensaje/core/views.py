from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class MensajeView(APIView):
    @swagger_auto_schema(
        operation_description="Devuelve un mensaje desde la API.",
        responses={200: openapi.Response('Mensaje retornado con éxito')}
    )
    def get(self, request):
        """
        Retorna un mensaje de prueba desde la API.
        """
        return Response({'mensaje': 'Este es un mensaje desde la API'}, status=status.HTTP_200_OK)
