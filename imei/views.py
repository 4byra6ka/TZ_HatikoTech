from adrf.decorators import api_view
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from imei.services import service_check_imei


@api_view(['POST'])
@permission_classes([IsAuthenticated])
async def check_imei(request):
    if 'imei' not in request.data:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Не задан IMEI'})
    else:
        imei = request.data['imei']
    data_imei = await service_check_imei(imei)
    if 'properties' in data_imei:
        return Response(data_imei['properties'])
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Внутренняя ошибка сервера'})
