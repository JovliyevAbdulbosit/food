from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver

# Create your models here.
from django.dispatch import receiver


class User(AbstractUser):
    username = models.CharField(max_length=50 , unique=True )
    is_costum = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)
    phone = models.CharField(max_length=20)
    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username
@receiver(post_save , sender = settings.AUTH_USER_MODEL)
def create_token(sender , instance=None , created = False , **kwargs):
    if created :
        Token.objects.create(user = instance)

class CostumModel(models.Model):
    user = models.OneToOneField(User ,related_name="teacher", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
class WorkerModel(models.Model):
    user = models.OneToOneField(User ,related_name="student", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.user.username