from api.models import Favorite
from api.models import Category
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class FavoriteSerializer(serializers.ModelSerializer):
    category = PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Favorite
        fields = ['title', 'description', 'ranking',
                  'metadata', 'category']

    def create(self, validated_data):
        category = Favorite.objects.filter(
            category=validated_data['category']
        ).count()
        if category >= validated_data['ranking'] or category <= validated_data['ranking']:
            validated_data['ranking'] = category + 1

            return super(FavoriteSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        category = Favorite.objects.filter(
            id=instance.pk,
            category=validated_data['category']
        ).get()
        if category.ranking >= validated_data['ranking'] or category.ranking <= validated_data['ranking']:
            validated_data['ranking'] = category.ranking

            return super(FavoriteSerializer, self).update(instance, validated_data)



