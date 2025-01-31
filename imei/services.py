import requests
import json

from django.conf import settings


async def service_check_imei(imei):
    url = 'https://api.imeicheck.net/v1/checks'
    headers = {
        'Authorization': 'Bearer ' + settings.TOKEN_IMEICHECK,
        'Content-Type': 'application/json'
    }
    body = json.dumps({
        "deviceId": imei,
        "serviceId": 12
    })
    response = requests.post(url, headers=headers, data=body)
    return response.json()
