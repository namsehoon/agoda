import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten
from users import models as user_models
from rooms import models as room_models
from reservations import models as reservation_models


NAME = "reservations"


class Command(BaseCommand):
    help = f"it is for create {NAME} like a boss"

    def add_arguments(self, parser):
        parser.add_argument("--numbers", default=1, type=int, help=f"how many {NAME}?")

    def handle(self, *args, **options):
        numbers = options.get("numbers")
        seeder = Seed.seeder()
        # 데이터베이스가 큰 경우에는 all로 가져오면 안되.
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            reservation_models.Reservation,
            numbers,
            {
                "guest": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(5, 20)),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{numbers} {NAME} created!"))
