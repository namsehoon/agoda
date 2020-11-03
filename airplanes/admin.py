from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Airplanes)
class AirplaneAdmin(admin.ModelAdmin):
    pass