import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "student_management_system.settings")
django.setup()

from main_app.models import CustomUser

email = "admin@gmail.com"
password = "admin123"

if not CustomUser.objects.filter(email=email).exists():
    CustomUser.objects.create_superuser(email=email, password=password)
    print("✅ Superuser created successfully.")
else:
    print("⚠️ Superuser already exists.")
