from rest_framework import serializers
from django.contrib.auth.models import Group, User
from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(read_only=True)
    power=serializers.IntegerField(read_only=True)
    color=serializers.CharField(read_only=True)
    numnber = serializers.CharField(read_only=True)
    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.power=validated_data.get('power', instance.power)
        instance.color=validated_data.get('color', instance.color)
        instance.save()
        return instance

    class Meta:
        model = Car
        fields = '__all__'

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']