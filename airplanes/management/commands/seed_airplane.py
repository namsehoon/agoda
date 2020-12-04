from django.core.management.base import BaseCommand
import random
from django_seed import Seed
from users import models as user_model
from airplanes import models as air_model

# 1.아무 어플에 management를 만들고 __init__.py 만들고,
# 2.management에 commands폴더 만들고, __init__.pya만들어줌
# 3.basecommand import해주고, add_arguments로 명령 만들어줌
# 4.handle 만ㄷ르어 준다음에 wows를 가져와서 출력해줌
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
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{numbers} user created!"))
