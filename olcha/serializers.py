from rest_framework import serializers

from olcha.models import Category,Group

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class GroupModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer(read_only=True)
    class Meta:
        model = Group
        fields = ['id','group_name','slug','category']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category,created = Category.objects.get_or_create(**category_data)
        group = Group.objects.create(category=category,**validated_data)


