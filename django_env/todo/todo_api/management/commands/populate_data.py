import json
import sys
import logging
from dateutil import parser
from django.core.management.base import BaseCommand
from todo_api.models import User
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Populating User data obtained in JSON from Monolith."

    def handle(self, *args, **options):
        for line in sys.stdin:
            data = json.loads(line)

            # Populating User Model
            if data["model"] == "User":
                user= User(
                    id=data["id"],
                    username=data["username"],
                    password=data["password"],
                    email=data["email"],
                    first_name=data["first_name"],
                    last_name=data["last_name"],
                    is_active=data["is_active"],
                    is_staff=data["is_staff"],
                    is_superuser=data["is_superuser"],
                    last_login=data["last_login"],
                    date_joined=data["date_joined"],
                )
                user.save()
                # logger.debug("User populated:{}".format(user.id))