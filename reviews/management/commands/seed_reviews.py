import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms import models as room_model
from reviews import models as reviews_model
from users import models as users_model


# 1.아무 어플에 management를 만들고 __init__.py 만들고,
# 2.management에 commands폴더 만들고, __init__.pya만들어줌
# 3.basecommand import해주고, add_arguments로 명령 만들어줌
# 4.handle 만ㄷ르어 준다음에 wows를 가져와서 출력해줌
class Command(BaseCommand):
    help = "it is for create reviews like a boss"

    def add_arguments(self, parser):
        parser.add_argument("--numbers", default=1, type=int, help="how many reviews?")

    def handle(self, *args, **options):
        numbers = options.get("numbers")
        seeder = Seed.seeder()
        # 데이터베이스가 큰 경우에는 all로 가져오면 안되.
        users = users_model.User.objects.all()
        print(users)
        rooms = room_model.Room.objects.all()

        seeder.add_entity(
            reviews_model.Review,
            numbers,
            {
                "user": lambda x: random.choice(users),
                "cleanliness": lambda x: random.randint(0, 10),
                "ancillary": lambda x: random.randint(0, 10),
                "location": lambda x: random.randint(0, 10),
                "service": lambda x: random.randint(0, 10),
                "satisfaction": lambda x: random.randint(0, 10),
                "room": lambda x: random.choice(rooms),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{numbers} reviews created!"))
