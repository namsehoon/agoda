from django.db import models
from core import models as core_model
from django_countries.fields import CountryField


class Airplane(core_model.TimeStampModel):

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
    ticket = models.CharField(max_length=50, null=True, choices=WAY_CHOICES)
    # 출발지, 목적지, 항공사
    starting_point = CountryField()
    destination = CountryField()
    flight_name = models.CharField(max_length=50, null=True, choices=FLIGHT_CHOICES)
    # 출국일, 귀국일, 시간대
    # TODO-------------------------------
    _departure = models.DateField(default="", null=True)
    _return = models.DateField(default="", null=True)
    # TODO-------------------------------
    # 인원
    adult = models.IntegerField()
    children = models.IntegerField()
    # 좌석 클래스
    flight_class = models.CharField(max_length=30, blank=True, choices=CLASS_CHOICES)
    users = models.ForeignKey(
        "users.User", related_name="airplanes", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.starting_point.name} to {self.destination.name}"
