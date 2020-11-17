from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    pass

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


# 룸에서 사진을 변경할 수 있음.
class photo_inline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ room admin """

    inlines = [
        photo_inline,
    ]

    # 커스텀 필드 세팅 (안)
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "descriptions",
                    "countries",
                    "city",
                    "price",
                    "address",
                ),
            },
        ),
        (
            "Room Option",
            {
                "fields": (
                    "room_type",
                    "beds",
                    "baths",
                    "guest",
                    "check_in",
                    "check_out",
                    "instant_book",
                    "host",
                )
            },
        ),
        (
            "Convenience",
            {
                # 접었다 폈다 할 수 있는 옵션
                # "classes": ("collapse",),
                "fields": ("amenities", "facilities", "houserule"),
            },
        ),
    )

    # 어드민 (밖)에서 보여지는거
    list_display = (
        "name",
        "price",
        "address",
        "beds",
        "baths",
        "guest",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    # 어드민 (밖)에서 옵셔널하게 걸러주는 필터 말그대로 ㅅ ㅋㅋㅋ
    list_filter = (
        "city",
        "price",
        "instant_book",
        "room_type",
        "amenities",
        "facilities",
        "houserule",
        "countries",
    )

    # 서치 바 fuck you know what im saying?
    search_fields = ("name", "amenities")

    # 이게 바로바로바로바로 many to many 에 적용하는거
    filter_horizontal = (
        "amenities",
        "facilities",
        "houserule",
    )

    # 많은 유저들을 운영할때 보기 쉽고, 간편하게 관리를 하기위해 외래키를 숫자로 준다.
    raw_id_fields = ("host",)

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """photo admin """

    list_display = (
        "__str__",
        "photos_thumnail",
    )

    def photos_thumnail(self, obj):

        return mark_safe(f"<img width=50px src='{obj.file.url}'></img>")