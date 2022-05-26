from django.contrib.auth.models import AbstractUser
from django.test import TestCase

# Create your tests here.
class User(AbstractUser):
    username = models.CharField(max_length=50 , unique=True )
    is_customer = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)
    phone = models.CharField(max_length=20)
    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username
@receiver(post_save , sender = settings.AUTH_USER_MODEL)
def create_token(sender , instance=None , created = False , **kwargs):
    if created :
        Token.objects.create(user = instance)

class TeacherModel(models.Model):
    user = models.OneToOneField(User ,related_name="teacher", on_delete=models.CASCADE)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    profession = models.CharField(max_length=40,blank=True , null=True)
    experience = models.TextField(blank=True , null=True)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
class StudentModel(models.Model):
    user = models.OneToOneField(User ,related_name="student", on_delete=models.CASCADE)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.user.username