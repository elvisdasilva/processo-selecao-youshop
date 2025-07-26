from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name