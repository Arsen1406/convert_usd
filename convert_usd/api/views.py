from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .get_convert import converter


@api_view(['GET'])
def convert_currency(request):
    """Основное представление. Мы получаем все данные,
    передаем в конвертер и возвращаем ответ клиенту."""
    currency_out = request.GET.get('from')
    currency_in = request.GET.get('to')
    value = request.GET.get('value')
    if currency_out is not None and currency_in is not None:
        result = converter(currency_out, currency_in, value)
        if isinstance(result, float):
            return Response({'result': result}, status=status.HTTP_200_OK)
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    return Response(
        'Не хватает одного аргумента',
        status=status.HTTP_400_BAD_REQUEST
    )
