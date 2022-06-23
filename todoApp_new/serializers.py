from rest_framework import serializers
from todoApp_new.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'date', 'completed']