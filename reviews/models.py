from django.db import models
from core import models as core_model

# Create your models here.


class Review(core_model.TimeStampModel):

    """ review model """

    review = models.TextField()
    cleanliness = models.IntegerField()
    ancillary = models.IntegerField()
    location = models.IntegerField()
    service = models.IntegerField()
    satisfaction = models.IntegerField()
    # 평점
    ten_score = models.BooleanField(default=False)
    five_score = models.BooleanField(default=False)
    one_score = models.BooleanField(default=False)

    # 유저와 리뷰, 방과 리뷰는 이어져있다.
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.room.name} - {self.review}"

    def review_average(self):
        avg = (
            self.cleanliness
            + self.ancillary
            + self.location
            + self.service
            + self.satisfaction
        ) / 5

        return round(avg, 2)

    review_average.short_description = "AVG."
