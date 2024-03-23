from rest_framework import generics
from rest_framework.views import APIView
from .models import Questionnew
from .serializers import QuestionnewSerializer
from rest_framework.response import Response
import random

class QuestionnewListCreate(APIView):
    def get(self, request, format=None):
        queryset = Questionnew.objects.filter(problem_id=random.randint(9900, 10000))
        serializer_class = QuestionnewSerializer(queryset, many=True)
        return Response(serializer_class.data)