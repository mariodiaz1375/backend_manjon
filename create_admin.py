import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings') # Revisa que sea 'core.settings'
django.setup()

User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('mario', 'admin@example.com', 'Mario1375')
    print("Superusuario creado con éxito")
else:
    print("El superusuario ya existe")