from django.db import models
from core import models as core_model


class List(core_model.TimeStampModel):

    """ list model """

    name = models.CharField(max_length=30)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", blank=True)

    def __str__(self):
        return self.name
