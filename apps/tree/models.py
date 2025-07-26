from django.db import models

from apps.account.models import Account


class Tree(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    scientific_name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = "Tree"
        verbose_name_plural = "Trees"
        ordering = ["name"]

    def __str__(self):
        return self.name


class PlantedTree(models.Model):
    age = models.IntegerField(null=False, blank=False)
    planted_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='planted_trees', blank=False, null=False)
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE, related_name='planted_trees', blank=False, null=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='planted_trees', blank=False, null=False)

    class Meta:
        verbose_name = "Planted Tree"
        verbose_name_plural = "Planted Trees"
        ordering = ['-planted_at']

    def __str__(self):
        return f"{self.tree.name} planted by {self.user.username} on {self.planted_at.strftime('%Y-%m-%d')}"