import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten
from users import models as user_models
from rooms import models as room_models
from lists import models as list_models


NAME = "list"


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
            list_models.List,
            numbers,
            {
                "user": lambda x: random.choice(users),
            },
        )
        create_pk = seeder.execute()
        # flatten으로 벗겨서 리스트 넣어줌
        find_pk = flatten(list(create_pk.values()))
        # 받아온 기본키를 각 룸에 할당 해줌
        for pk in find_pk:
            list_model = list_models.List.objects.get(pk=pk)
            to_add = rooms[random.randint(1, 4) : random.randint(6, 9)]  # 배열을 제한;
            list_model.rooms.add(*to_add)  # 리스트안에있는 룸필드(manytomany)에 추가하는데, to_add참고하여
            # 에러:int() argument must be a string, a bytes-like object or a number, not 'QuerySet' 해결: 추가 "*"
        self.stdout.write(self.style.SUCCESS(f"{numbers} {NAME} created!"))
