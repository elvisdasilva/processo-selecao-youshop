from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from apps.account.models import Account
from django.contrib.auth.models import User

from apps.tree.models import PlantedTree, Tree
from apps.user.models import UserExtension


class PlantedTreeBaseTestCase(TestCase):
    def setUp(self):
        # create accounts
        self.account_a = Account.objects.create(name="Group A", active=True)
        self.account_b = Account.objects.create(name="Group B", active=False)

        # create users
        self.user_a = User.objects.create_user(
            username="user_a", password="password123"
        )
        self.user_b = User.objects.create_user(
            username="user_b", password="password123"
        )
        self.user_c = User.objects.create_user(
            username="user_c", password="password123"
        )

        # create a user extension
        self.ext_a = UserExtension.objects.create(user=self.user_a)
        self.ext_b = UserExtension.objects.create(user=self.user_b)
        self.ext_c = UserExtension.objects.create(user=self.user_c)

        # create a link between the user and the account
        self.ext_a.account.add(self.account_a)
        self.ext_b.account.add(self.account_b)
        self.ext_c.account.add(self.account_a)

        # create trees
        self.tree_a = Tree.objects.create(
            name="Ipê-amarelo", scientific_name="Handroanthus albus"
        )
        self.tree_b = Tree.objects.create(
            name="Pau-brasil", scientific_name="Paubrasilia echinata"
        )
        self.tree_c = Tree.objects.create(
            name="Hortelã", scientific_name="Mentha spicata"
        )

        # create planted trees
        self.planted_tree_a = PlantedTree.objects.create(
            tree=self.tree_a,
            age=5,
            user=self.user_a,
            account=self.account_a,
            planted_at=timezone.now(),
            location_latitude=12.345678,
            location_longitude=98.765432,
        )

        self.planted_tree_b = PlantedTree.objects.create(
            tree=self.tree_b,
            age=10,
            user=self.user_b,
            account=self.account_b,
            planted_at=timezone.now(),
            location_latitude=23.456789,
            location_longitude=87.654321,
        )

        self.planted_tree_c = PlantedTree.objects.create(
            tree=self.tree_c,
            age=2,
            user=self.user_c,
            account=self.account_a,
            planted_at=timezone.now(),
            location_latitude=34.567890,
            location_longitude=76.543210,
        )

    def test_template_renders_planted_trees_for_logged_user(self):
        self.client.login(username="user_a", password="password123")
        response = self.client.get(reverse("planted_tree_list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "planted_tree/planted_tree.html")
        self.assertContains(response, "Ipê-amarelo")
        self.assertNotContains(response, "Hortelã")

    def test_template_403_when_accessing_trees_of_other_user(self):
        self.client.login(username="user_a", password="password123")

        response = self.client.get(
            reverse("planted_tree_update", args=[self.user_b.id])
        )

        self.assertEqual(response.status_code, 403)

    def test_template_lists_trees_of_users_from_same_account(self):
        self.client.login(username="user_a", password="password123")
        response = self.client.get(reverse("user_accounts_planted_tree_list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "planted_tree/user_accounts_planted_tree.html"
        )
        self.assertContains(response, "Ipê-amarelo")
        self.assertContains(response, "Hortelã")
        self.assertNotContains(response, "Pau-brasil")
