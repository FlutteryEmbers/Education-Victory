from django.urls import path
from .views import QuestionnewListCreate

urlpatterns = [
    path('questionnew', QuestionnewListCreate.as_view(), name='questionnew-list-create'),
]