# skills/serializers.py
from rest_framework import serializers
from .models import Skill, UserInput

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'track']

class UserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInput
        fields = ['id','track', 'description']
