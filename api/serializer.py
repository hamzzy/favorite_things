from api.models import Favorite
from api.models import Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('title', 'description', 'ranking',
                  'metadata', 'category', 'created_at', 'modified_at')
