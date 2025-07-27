from apps.tree.models import PlantedTree
from rest_framework import serializers


class PlantedTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantedTree
        fields = '__all__'