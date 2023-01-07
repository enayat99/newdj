from backend.models import FoodCategory,Food,FavoriteFoods
from rest_framework import serializers
from rest_framework.serializers import FileField, Serializer


class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        image = FileField()
        model = FoodCategory
        fields = '__all__'


class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        image=FileField()
        model=Food
        fields='__all__'

class FavoriteFoodSerializers(serializers.ModelSerializer):
    class Meta:
        image=FileField()
        model=FavoriteFoods
        fields='__all__'