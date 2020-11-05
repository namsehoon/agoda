from django.contrib import admin
from . import models


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """ conversation admin """

    pass


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """ message admin """

    pass