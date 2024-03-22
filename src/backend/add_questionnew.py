import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EX.settings')
django.setup()

from problemnew.models import Problemnew  # Adjust the import according to your project structure
from questionnew.models import Questionnew
from utils.tools import Random_Generator

from problem.models import Problem
from question.models import ChoiceQuestion, CodingQuestion

rg = Random_Generator(seed=10)
def add_question():
    '''
    problem = Problem()
    problem.save()

    question = ChoiceQuestion(problem=problem)
    question.save()
    '''
    problem = Problem.objects.create(name=rg.sample_one(80))
    problem.save()
    question1 = ChoiceQuestion.objects.create(problem=problem, answer_type=0, text_hint=rg.sample_one(500))
    question1.save()
    question2 = CodingQuestion.objects.create(problem=problem, default_code=rg.sample_one(3000), answer=rg.sample_one(2000))
    question2.save()
    question3 = ChoiceQuestion.objects.create(problem=problem, answer_type=1, text_hint=rg.sample_one(500))
    question3.save()

def add_questionnew():
    problem = Problemnew(title=rg.sample_one(128), remark=rg.sample_one(128))
    problem.save()
    question1 = Questionnew.objects.create(problem=problem, type=1, payload=rg.generate_random_json(), title=rg.sample_one(128))
    question1.save()
    question2 = Questionnew.objects.create(problem=problem, type=2, payload=rg.generate_random_json(), title=rg.sample_one(128))
    question2.save()
    question3 = Questionnew.objects.create(problem=problem, type=3, payload=rg.generate_random_json(), title=rg.sample_one(128))
    question3.save()
    question4 = Questionnew.objects.create(problem=problem, type=4, payload=rg.generate_random_json(), title=rg.sample_one(128))
    question4.save()
    # Creating an Author instance
    '''
    problem2 = Problemnew(title='sadgasdfadsgasd', remark='sadgasdfaewqrdafsdag')
    problem2.save()

    # Creating a Book instance and linking it to the author
    q1 = Question2(title='dasgfdsgasdfsdaf', type=1, problem=problem2, payload={"key": "value", "list": [1, 2, 3]}, stage=1)
    q1.save()

    q2 = Question2(title='dasgfdsgasdfsdaf', type=2, problem=problem2, payload={"key": "value", "list": [1, 2, 3]}, stage=1)
    q2.save()

    q3 = Question2(title='dasgfdsgasdfsdaf', type=3, problem=problem2, payload={"key": "value", "list": [1, 2, 3]}, stage=1)
    q3.save()

    q4 =  Question2(title='dasgfdsgasdfsdaf', type=4, problem=problem2, payload={"key": "value", "list": [1, 2, 3]}, stage=1)
    q4.save()
    '''

if __name__ == '__main__':
    N = 10_000_000
    for i in range(N):
        add_question()
        add_questionnew()
        