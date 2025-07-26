from django.contrib import admin

from apps.account.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("name", "active", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("active",)
