# -*- coding: utf-8 -*-

from rest_framework import serializers
from db.models import Person


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    age = serializers.IntegerField()
    birth = serializers.DateField()

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.age = validated_data.get('age',instance.age)
        instance.birth = validated_data.get('birth',instance.birth)
        instance.save()
        return instance
