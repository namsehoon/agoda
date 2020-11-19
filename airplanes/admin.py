from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Airplane)
class AirplaneAdmin(admin.ModelAdmin):
    """ airplane admin """

    list_display = (
        "__str__",
        "flight_class",
        "reservation_name",
    )

    def reservation_name(self, obj):
        return obj.users.username
