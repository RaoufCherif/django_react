from rest_framework import serializers
from .models import Todo_lists


class Todo_listsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo_lists
        fields = ('title', 'description', 'completed')