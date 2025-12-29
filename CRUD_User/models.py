from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.
class User(models.Model):
  user_id = models.CharField(max_length=20)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  designation = models.CharField(max_length=50)


@receiver(post_save , sender=User)
def create_user_api(sender, instance, created, **kwargs):
  print("*"*30)
  print("User object Created")
  print("*"*30)

@receiver(post_delete, sender=User)
def delete_user_api(sender, instance, **kwargs):
  print("*"*30)
  print("User object Deleted")
  print("*"*30)