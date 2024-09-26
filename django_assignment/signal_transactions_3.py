from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal handler
@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    if transaction.get_connection().in_atomic_block:
        print("Signal handler running inside a transaction.")
    else:
        print("Signal handler NOT running inside a transaction.")

# Example function to create a user
def create_user():
    with transaction.atomic():
        print("Creating user inside a transaction...")
        user = User.objects.create(username='test_user')

create_user()


