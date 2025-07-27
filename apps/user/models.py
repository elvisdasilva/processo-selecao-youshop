from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from typing import Tuple
from apps.account.models import Account
from apps.tree.models import PlantedTree, Tree


class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extension', blank=False, null=False)
    account = models.ManyToManyField(Account, related_name='users', blank=False)
    bio = models.TextField(blank=True, null=True)

    def plant_tree(self, tree, account, age, latitude, longitude):
        planted_tree = PlantedTree.objects.create(
            user=self.user,
            tree=tree,
            account=account,
            location_latitude=Decimal(latitude),
            location_longitude=Decimal(longitude),
            age=age
        )
        return planted_tree
    
    def plant_trees(self, tree_data_list):
        planted_trees = []
        for tree in tree_data_list:
            planted_tree = self.plant_tree(
                tree=tree["tree"],
                account=tree["account"],
                age=tree["age"],
                latitude=tree["latitude"],
                longitude=tree["longitude"],
            )
            planted_trees.append(planted_tree)
        return planted_trees