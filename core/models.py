from django.db import models


class TimeStampModel(models.Model):

    """ timestamp model (모델확장용) """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """ 기타사항, 데이터베이스 저장 X """

        abstract = True
