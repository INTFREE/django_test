from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
# Create your models here.


class AuthUserManager(BaseUserManager):
    def create_user(self, weixin_name, weixin_data, password=None):
        if not weixin_name:
            raise ValueError('must have weixin_name')

        user = self.model(
            weixin_name=weixin_name,
            weixin_data=weixin_data
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, weixin_name, weixin_data, password):
        user = self.create_user(weixin_name, weixin_data=weixin_data, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class AuthUser(AbstractBaseUser, PermissionsMixin):
    weixin_name = models.CharField(max_length=30, unique=True)
    weixin_data = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_adimin = models.BooleanField(default=False)

    objects = AuthUserManager()

    USERNAME_FIELD = 'weixin_name'
    REQUIRED_FIELDS = ['weixin_data']

    def get_full_name(self):
        return self.weixin_name

    def get_short_name(self):
        return self.weixin_name

    def __str__(self):
        return self.weixin_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_adimin