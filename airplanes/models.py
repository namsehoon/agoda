from django.db import models
from core import models as core_model
from django_countries.fields import CountryField
from django.utils import timezone


class Airplanes(core_model.TimeStampModel):

    """ airplanes model """

    WAY_ONEWAY = "oneway"
    WAY_ROUNDTRIP = "roundtrip"

    WAY_CHOICES = (
        (WAY_ONEWAY, "One Way"),
        (WAY_ROUNDTRIP, "Round Trip"),
    )

    FLIGHT_1 = "daehan"
    FLIGHT_2 = "asiana"
    FLIGHT_3 = "jeju"
    FLIGHT_4 = "airforce"

    FLIGHT_CHOICES = (
        (FLIGHT_1, "Daehan"),
        (FLIGHT_2, "Asiana"),
        (FLIGHT_3, "Jeju"),
        (FLIGHT_4, "Airforce"),
    )

    CLASS_ECONOMY = "economy"
    CLASS_BUSINESS = "business"
    CLASS_FIRSTCLASS = "firstclass"

    CLASS_CHOICES = (
        (CLASS_ECONOMY, "Economy"),
        (CLASS_BUSINESS, "Business"),
        (CLASS_FIRSTCLASS, "First Class"),
    )

    # 편도, 왕복
    name = models.CharField(max_length=50, null=True, choices=WAY_CHOICES)
    # 출발지, 목적지, 항공사
    starting_point = CountryField()
    destination = CountryField()
    flight_name = models.CharField(max_length=50, null=True, choices=FLIGHT_CHOICES)
    # 출국일, 귀국일, 시간대
    # TODO-------------------------------
    _departure = models.TimeField(default=date.today)
    _return = models.TimeField(default=date.today)
    take_time = models.TimeField(default=date.today)
    # TODO-------------------------------
    # 인원
    adult = models.IntegerField(default=0)
    children = models.IntegerField(default=0)
    # 좌석 클래스
    flight_class = models.CharField(max_length=30, blank=True, choices=CLASS_CHOICES)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)