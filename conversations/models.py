from django.db import models
from core import models as core_model


class Conversation(core_model.TimeStampModel):

    """ conversation model """

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        username = []
        for user in self.participants.all():
            username.append(user.username)
        return " , ".join(username)


class Message(core_model.TimeStampModel):
    """ message model """

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says : {self.message}"
