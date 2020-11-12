from django.contrib import admin
from . import models


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """ conversation admin """

    filter_horizontal = ("participants",)


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """ message admin """

    list_display = ("__str__", "created")