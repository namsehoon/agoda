from django.core.management.base import BaseCommand
from rooms.models import Amenity

# 1.아무 어플에 management를 만들고 __init__.py 만들고,
# 2.management에 commands폴더 만들고, __init__.pya만들어줌
# 3.basecommand import해주고, add_arguments로 명령 만들어줌
# 4.handle 만ㄷ르어 준다음에 wows를 가져와서 출력해줌
class Command(BaseCommand):
    help = "it is for create amenities like a boss"

    """ def add_arguments(self, parser):
        parser.add_argument("--wows", help="how many time?")"""

    def handle(self, *args, **options):
        amenities = [
            "Air conditioning",
            "Alarm Clock",
            "Balcony",
            "Bathroom",
            "Bathtub",
            "Bed Linen",
            "Boating",
            "Cable TV",
            "Carbon monoxide detectors",
            "Chairs",
            "Children Area",
            "Coffee Maker in Room",
            "Cooking hob",
            "Cookware & Kitchen Utensils",
            "Dishwasher",
            "Double bed",
            "En suite bathroom",
            "Free Parking",
            "Free Wireless Internet",
            "Freezer",
            "Fridge / Freezer",
            "Golf",
            "Hair Dryer",
            "Heating",
            "Hot tub",
            "Indoor Pool",
            "Ironing Board",
            "Microwave",
            "Outdoor Pool",
            "Outdoor Tennis",
            "Oven",
            "Queen size bed",
            "Restaurant",
            "Shopping Mall",
            "Shower",
            "Smoke detectors",
            "Sofa",
            "Stereo",
            "Swimming pool",
            "Toilet",
            "Towels",
            "TV",
        ]
        for a in amenities:
            Amenity.objects.create(name=a, description=a)
        self.stdout.write(self.style.SUCCESS("AMENITY CREATED"))
