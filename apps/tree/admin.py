from django.contrib import admin

from apps.tree.models import PlantedTree, Tree


class PlantedTreeInline(admin.TabularInline):
    model = PlantedTree
    extra = 0
    readonly_fields = ("age", "user", "account", "location_latitude", "location_longitude")
    fields = ("age", "user", "location_latitude", "location_longitude")
    can_delete = False
    max_num = 0


@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    list_display = ("name", "scientific_name")
    search_fields = ("name", "scientific_name")
    inlines = [PlantedTreeInline]
