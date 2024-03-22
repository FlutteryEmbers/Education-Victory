from rest_framework import serializers
from .models import Questionnew

class QuestionnewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnew
        fields = ['id', 'title', 'type', 'problem', 'payload', 'stage']