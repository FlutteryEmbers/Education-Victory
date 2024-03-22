from rest_framework import generics
from .models import Questionnew
from .serializers import QuestionnewSerializer

class QuestionnewListCreate(generics.ListCreateAPIView):
    queryset = Questionnew.objects.filter(problem_id=1000)
    serializer_class = QuestionnewSerializer