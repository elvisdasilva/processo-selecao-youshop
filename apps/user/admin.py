from django.contrib import admin

from apps.user.models import User, UserExtension
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserExtensionAdmin(admin.StackedInline):
    model = UserExtension
    can_delete = False
    verbose_name_plural = "User Extension"
    filter_horizontal = ("account",)


class UserAdmin(BaseUserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "get_accounts",
        "is_staff",
    )
    inlines = (UserExtensionAdmin,)

    def get_accounts(self, obj):
        return (", ".join([account.name for account in obj.extension.account.all()]) if obj.extension else "No Accounts")

    get_accounts.short_description = "Accounts"


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
