import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'standalone.settings')
django.setup()
from example.models import Person

new_person = Person(name='Durmus')
new_person.save()

