# from django.db import models
# from django.contrib.auth.models import AbstractUser, AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
# from django.utils import timezone
# #from .managers import CustomUserManager
#
#
# # Create your models here.
#
# # class CustomUser(AbstractUser):
# #     username = None
# #     email = models.EmailField(unique=True)
# #
# #     USERNAME_FIELD = 'email'
# #     REQUIRED_FIELDS = []
# #
# #     objects = CustomUserManager()
# #
# #     def __str__(self):
# #         return self.email
#
# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     class Meta:
#         db_table = 'auth_user'
#     email = models.EmailField(unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(default=timezone.now)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     objects = CustomUserManager()
#
#     def __str__(self):
#         return self.email
