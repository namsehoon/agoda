import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten
from users.models import User
from rooms import models as room_model


# 1.아무 어플에 management를 만들고 __init__.py 만들고,
# 2.management에 commands폴더 만들고, __init__.pya만들어줌
# 3.basecommand import해주고, add_arguments로 명령 만들어줌
# 4.handle 만ㄷ르어 준다음에 wows를 가져와서 출력해줌
class Command(BaseCommand):
    help = "it is for create rooms like a boss"

    def add_arguments(self, parser):
        parser.add_argument("--numbers", default=1, type=int, help="how many rooms?")

    def handle(self, *args, **options):
        numbers = options.get("numbers")
        seeder = Seed.seeder()
        # 데이터베이스가 큰 경우에는 all로 가져오면 안되.
        users = User.objects.all()
        room_type = room_model.RoomType.objects.all()
        seeder.add_entity(
            room_model.Room,
            numbers,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(users),
                "room_type": lambda x: random.choice(room_type),
                "beds": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
                "guest": lambda x: random.randint(1, 5),
                "price": lambda x: random.randint(1, 300),
            },
        )
        find_rooms = seeder.execute()
        # flatten으로 벗겨서 리스트 넣어줌
        create_rooms = flatten(list(find_rooms.values()))
        # 받아온 기본키를 각 룸에 할당 해줌
        for pk in create_rooms:
            room = room_model.Room.objects.get(pk=pk)
            for i in range(3, random.randint(8, 10)):
                room_model.Photo.objects.create(
                    file=f"/room_photos/{random.randint(1,39)}.jpeg",
                    room=room,
                    description=seeder.faker.sentence(),
                )

        self.stdout.write(self.style.SUCCESS(f"{numbers} rooms created!"))
