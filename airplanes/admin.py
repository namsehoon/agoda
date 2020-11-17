from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Airplane)
class AirplaneAdmin(admin.ModelAdmin):
    """ airplane admin """

    list_display = (
        "__str__",
        "flight_class",
        "user_count",
    )