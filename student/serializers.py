from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
    rollno=serializers.IntegerField()
    name=serializers.CharField(max_length=30)
    city=serializers.CharField(max_length=40)
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    def update(self, instance, validated_data):
        print(instance.name)
        instance.name=validated_data.get('name',instance.name)
        print(instance.name)
        instance.rollno = validated_data.get('rollno', instance.rollno)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
