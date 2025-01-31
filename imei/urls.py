from django.urls import path

from imei.apps import ImeiConfig
from imei.views import check_imei

app_name = ImeiConfig.name

urlpatterns = [
    path("check-imei/", check_imei, name="check_imei"),
]
