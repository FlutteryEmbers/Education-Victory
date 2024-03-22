from django.urls import path
from .views import QuestionListCreate

urlpatterns = [
    path('questionold', QuestionListCreate.as_view(), name='question-list-create'),
]