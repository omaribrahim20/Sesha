from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='profile',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='Name')

    @staticmethod
    def create_user_profile(user_object):
        UserProfile.objects.create(user=user_object)

    def __str__(self):
        return self.user.username


class BaseUser(AbstractUser):
    def save(self, *args, **kwargs):
        user_object = super(BaseUser, self).save(self, *args, **kwargs)
        UserProfile.objects.create(user=user_object)
        return user_object

