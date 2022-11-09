from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(post_save, sender=User)
def createProfile(sender,instance, created, **kwargs):
    if created:
        user=instance
        print(user)
        profile = Profile.objects.create(
            user = user,
            nickname = user.username,
        )

    

@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

