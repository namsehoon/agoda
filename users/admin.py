from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


# decorator 어드민이 모델을 어떻게 보여주는지, 어떻게 작동해야하는지 알려준다.
@admin.register(models.User)
class MyUserAdmin(UserAdmin):
    """ User Admin """

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