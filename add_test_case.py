import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EX.settings')
django.setup()

from problem2.models import Problem2  # Adjust the import according to your project structure
from question2.models import Question2

from problem.models import Problem
from question.models import ChoiceQuestion

def add_test_data_type1():
    problem = Problem()
    problem.save()

    question = ChoiceQuestion(problem=problem)
    question.save()

def add_test_data_type2():
    # Creating an Author instance
    problem2 = Problem2(title='sadgasdfadsgasd', remark='sadgasdfaewqrdafsdag')
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


if __name__ == '__main__':
    for i in range(1000000):
        add_test_data_type1()

    for i in range(1000000):
        add_test_data_type2()