from django.core.management.base import BaseCommand
import random
from datetime import datetime, timedelta
from django_seed import Seed
from users import models as user_model
from airplanes import models as air_model


class Command(BaseCommand):
    help = "it is for create airplane like a boss"

    def add_arguments(self, parser):
        parser.add_argument("--numbers", default=1, type=int, help="how many airplane?")

    def handle(self, *args, **options):
        numbers = options.get("numbers")
        seeder = Seed.seeder()
        user = user_model.User.objects.all()
        seeder.add_entity(
            air_model.Airplane,
            numbers,
            {
                "adult": lambda x: random.randint(0, 5),
                "children": lambda x: random.randint(0, 5),
                "users": lambda x: random.choice(user),
                "_departure": lambda x: datetime.now  # 모듈(필드)에 출발시간:지금 + timedeleta를 사용해 일 수를 더해준다.
                + timedelta(days=random.randint(2, 5)),
                "_return": lambda x: datetime.now()
                + timedelta(days=random.randint(7, 20)),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{numbers} airplane created!"))
