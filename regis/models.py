from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.


class ManagerUser(BaseUserManager):
    def create_user(self, username, password, is_active=True, is_superuser=False, is_staff=False, *args, **kwargs):
        user = self.model(username=username,
                          password=password,
                          is_active=is_active,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          **kwargs)
        user.set_password(password)
        return user.save()

    def create_superuser(self, username, password, **kwargs):
        return self.create_user(username, password, is_superuser=True, is_staff=True, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    username = models.CharField(max_length=128, unique=True)
    phone = models.CharField(max_length=20)
    data_joined = models.DateTimeField(editable=False, auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "username"
    objects = ManagerUser()
    REQUIRED_FIELDS = ['phone']

    def format(self):
        return {
            "id": self.id,
            "phone": self.phone,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.first_name,
            "is_staff": self.is_staff,
            "data_joined": self.data_joined,
            "is_active": self.is_active,
            "is_superuser": self.is_superuser,
        }

    def __str__(self):
        return self.username





