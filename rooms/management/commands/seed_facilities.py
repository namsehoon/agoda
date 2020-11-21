from django.core.management.base import BaseCommand
from rooms.models import Facility

# 1.아무 어플에 management를 만들고 __init__.py 만들고,
# 2.management에 commands폴더 만들고, __init__.pya만들어줌
# 3.basecommand import해주고, add_arguments로 명령 만들어줌
# 4.handle 만ㄷ르어 준다음에 wows를 가져와서 출력해줌
class Command(BaseCommand):
    help = "it is for create amenities like a boss"

    """ def add_arguments(self, parser):
        parser.add_argument("--wows", help="how many time?")"""

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for a in facilities:
            Facility.objects.create(name=a, description=a)
        self.stdout.write(self.style.SUCCESS("Facility CREATED"))
