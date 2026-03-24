from rest_framework import serializers
from .models import MenuCategory

class MenuCategorySerializer(serializers.MenuSerializer):
    class Meta:
        model = MenuCategory
        fields = ["name"]