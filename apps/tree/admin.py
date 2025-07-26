from django.contrib import admin

from apps.tree.models import PlantedTree, Tree


class PlantedTreeInline(admin.TabularInline):
    model = PlantedTree
    extra = 1
    readonly_fields = ("age", "user", "account")
    fields = ("age", "user",)
    can_delete = False


@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    list_display = ("name", "scientific_name")
    search_fields = ("name", "scientific_name")
    inlines = [PlantedTreeInline]
