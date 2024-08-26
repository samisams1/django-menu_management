from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.all(), required=False, allow_null=True)
    depth = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ('id', 'name', 'parent', 'depth', 'children')
        children = serializers.SerializerMethodField()
        

    def get_depth(self, obj):
        if obj.parent:
            return obj.parent.depth + 1
        else:
            return 1

    def get_children(self, obj):
        return MenuSerializer(obj.get_children(), many=True).data

    def create(self, validated_data):
        parent = validated_data.pop('parent', None)
        instance = Menu.objects.create(parent=parent, **validated_data)
        return instance

    def update(self, instance, validated_data):
        parent = validated_data.pop('parent', None)
        instance.parent = parent
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance