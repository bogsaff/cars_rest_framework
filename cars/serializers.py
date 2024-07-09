from rest_framework import serializers

from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(read_only=True)
    power=serializers.IntegerField(read_only=True)
    color=serializers.CharField(read_only=True)

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.power=validated_data.get('power', instance.power)
        instance.color=validated_data.get('color', instance.color)
        instance.save()
        return instance
