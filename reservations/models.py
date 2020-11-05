from django.db import models
from core import models as core_model

# Create your models here.


class Reservation(core_model.TimeStampModel):
    """ reservation model """

    STATUS_PENDING = "peding"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )
    # TODO => 여기다가 나중에 placeholder 넣기 : select
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Select",
    )
    check_in = models.DateField()
    check_out = models.DateField()

    # one to many OR many to mnay
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"
