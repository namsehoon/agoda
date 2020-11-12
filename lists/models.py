from django.db import models
from core import models as core_model


class List(core_model.TimeStampModel):

    """ list model """

    name = models.CharField(max_length=30)
    user = models.ForeignKey(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    rooms = models.ManyToManyField("rooms.Room", related_name="lists", blank=True)

    def __str__(self):
        return self.name

    def rooms_count(self):
        return self.rooms.count()

    rooms_count.short_description = "Number Of Rooms"