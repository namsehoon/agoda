from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as room_model
from airplanes import models as airplanes_model

# Register your models here.


class inline_room(admin.TabularInline):
    model = room_model.Room


class inline_airplane(admin.TabularInline):
    model = airplanes_model.Airplane


# decorator 어드민이 모델을 어떻게 보여주는지, 어떻게 작동해야하는지 알려준다.
@admin.register(models.User)
class MyUserAdmin(UserAdmin):
    """ User Admin """

    inlines = [inline_room, inline_airplane]

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthday",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "superhost",
        "airplain_users",
    )

    def airplain_users(self, obj):
        return obj.airplanes.count()

    airplain_users.short_description = "Tickets"
