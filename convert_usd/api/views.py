from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ConvertSerializer
from rest_framework.views import APIView

from .get_convert import converter


@api_view(['GET'])
def convert_valute(request):
    valute_out = request.data.get('valute_out')
    valute_in = request.data.get('valute_in')
    count = request.data.get('count')
    serializer = ConvertSerializer(converter(valute_out, valute_in, count))
    if valute_out is not None and valute_in is not None:
        return Response(serializer, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
