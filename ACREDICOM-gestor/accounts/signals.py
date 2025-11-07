
from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from .models import Profile

ADMIN_GROUP = 'ADMINISTRADOR'
USER_GROUP = 'USUARIO'

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    for name in [ADMIN_GROUP, USER_GROUP]:
        Group.objects.get_or_create(name=name)

@receiver(post_save, sender=User)
def create_profile_and_default_group(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        user_group = Group.objects.get(name=USER_GROUP)
        instance.groups.add(user_group)
