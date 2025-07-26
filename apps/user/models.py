from django.db import models
from django.contrib.auth.models import User

from apps.account.models import Account


class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extension', blank=False, null=False)
    account = models.ManyToManyField(Account, related_name='users', blank=False, null=False)