from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Todo, TimingTodo
import re

class TimingTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimingTodo
        exclude = ['created_at', 'updated_at']

class TodoSerializer(serializers.ModelSerializer):  
    timingtodos = TimingTodoSerializer(many=True, read_only=True)
    slug = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ['user', 'uid', 'todo_title', 'slug', 'todo_description', 'is_done', 'timingtodos'] # includes some necessary model fields: title, description etc that is required by client or developer.
#       exclude = ['created_at'] #when you have more fields supose 100 and one field don't want to show but others want to show than have to use exclude just to write which fields you don't want to show.
#       fields = '__all__'  # includes all model fields: uid, title, etc.

    def get_slug(self, obj):
        return slugify(obj.todo_title) # can return anything like a name "proma" or none.

    def validate_todo_title(self, data):
        # Check if value exists (can skip this; DRF already handles required=True)
        if data:
            # Length check
            if len(data) <= 3:
                raise serializers.ValidationError("todo_title must be longer than 3 characters.")

            # Special character check
            regex = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')
            if regex.search(data):
                raise serializers.ValidationError("todo_title cannot contain special characters.")

        return data