from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    """ USER MODEL CLASS """

    GENTER_MALE = "male"
    GENDER_FAMALE = "famale"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENTER_MALE, "Male"),
        (GENDER_FAMALE, "Feamale"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"
    LANGUAGE_OTHERS = "others"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
        (LANGUAGE_OTHERS, "Others"),
    )

    CURRENCY_ENGLISH = "usd"
    CURRENCY_KOREA = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_ENGLISH, "USD"),
        (CURRENCY_KOREA, "KRW"),
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        max_length=50, blank=True, null=True, choices=GENDER_CHOICES
    )
    bio = models.TextField(default="", blank=True)
    birthday = models.DateField(null=True, blank=True)
    language = models.CharField(
        max_length=10, blank=True, null=True, choices=LANGUAGE_CHOICES
    )
    currency = models.CharField(
        max_length=10, blank=True, null=True, choices=CURRENCY_CHOICES
    )
    superhost = models.BooleanField(default=False)
