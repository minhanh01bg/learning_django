import json
import sys
from django.core.management.base import BaseCommand
from django.core.serializers.json import DjangoJSONEncoder
from todo_api.models import User
class Command(BaseCommand):
    help = "Extracting user data to JSON format"

    def handle(self, *args, **options):
        # Get User Data from User Model in monolith        
        user_microservice_data = User.objects.all()
        for user_data in user_microservice_data:
            data = {
                "model": "User",
                "id": user_data.id,
                "username": user_data.username,
                "password": user_data.password,
                "email": user_data.email,
                "first_name": user_data.first_name,
                "last_name": user_data.last_name,
                "is_active": user_data.is_active,
                "is_staff": user_data.is_staff,
                "is_superuser": user_data.is_superuser,
                "last_login": user_data.last_login,
                "date_joined": user_data.date_joined,
            }
            # Dumping Data into JSON Format
            json.dump(data, sys.stdout, cls=DjangoJSONEncoder)
            sys.stdout.write("\n")
