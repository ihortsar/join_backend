from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Task
        fields = "__all__"
