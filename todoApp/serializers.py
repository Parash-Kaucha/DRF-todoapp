from rest_framework import serializers
from todoApp.models import ToDo

class ToDoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=1000)
    date = serializers.DateTimeField(default_timezone=None)
    completed = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return ToDo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.date = validated_data.get('date', instance.date)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
        return instance

#Field Level Validation
def validate_title(self, value):
        if len(value) < 4:
            raise serializers.ValidationError('title length must be atlest 4')
        return value

def validate_completed(self, value):
        if value != False:
            raise serializers.ValidationError('todos mustnot be completed')
        return value

#Object Level Validation
def validate(self, data):
    tl = data.get('title')
    cp = data.get('completed')
    if len('tl')<4 and cp!=False:
        raise serializers.ValidationError('Completion status must not be true')
    return data

