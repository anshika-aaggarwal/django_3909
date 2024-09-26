import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal handler
@receiver(post_save, sender=User)
def slow_signal_handler(sender, instance, **kwargs):
    print("Signal received, starting processing...")
    time.sleep(5)  # Simulating a slow process
    print("Signal processing done.")

# Example function to create a user
def create_user():
    print("Creating user...")
    user = User.objects.create(username='test_user')
    print("User creation complete.")

create_user()


