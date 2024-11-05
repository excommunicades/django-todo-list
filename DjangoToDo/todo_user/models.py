from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class ToDoUserManager(BaseUserManager):

    def get_by_natural_key(self, username):

        return self.get(username=username)


class ToDoUser(AbstractBaseUser, PermissionsMixin):

    """ToDo user model"""

    # first_name = models.CharField(max_length=30, blank=False, null=False)
    # last_name = models.CharField(max_length=30, blank=False, null=False)

    username = models.CharField(
                            max_length=30,
                            blank= False,
                            null=False,
                            unique=True,
                            )

    email = models.EmailField(
                        unique=True,
                        blank=False,
                        null=False,
                        )

    password = models.CharField(
                            max_length=128,
                            blank=False,
                            null=False,
                            )

    # age = models.SmallIntegerField()
    # date_of_birth = models.DateField(null=True, blank=True)
    # is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = ToDoUserManager()
