from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
def create_user(self, email, username, password=None):
if not email:
raise ValueError("Пользователь должен иметь адрес электронной почты")
email = self.normalize_email(email)
user = self.model(email=email, username=username)
user.set_password(password)
user.save(using=self._db)
return user

def create_superuser(self, email, username, password=None):
user = self.create_user(email, username, password)
user.is_staff = True
user.is_superuser = True
user.save(using=self._db)
return user

class CustomUser(AbstractBaseUser):
email = models.EmailField(unique=True)
username = models.CharField(max_length=150, unique=True)
is_active = models.BooleanField(default=True)
is_staff = models.BooleanField(default=False)

USERNAME_FIELD = 'email'
REQUIRED_FIELDS = ['username']

objects = CustomUserManager()

def __str__(self):
return self.email
