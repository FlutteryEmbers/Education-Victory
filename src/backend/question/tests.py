from django.test import TestCase
from .models import ChoiceQuestion
from problem.models import Problem
import time

class MyModelTestCase(TestCase):
    def setUp(self):
        print('start setting up')
        for i in range(10_000_000):
            problem = Problem.objects.create()
            question = ChoiceQuestion.objects.create(problem=problem)
        

    def test_query_my_model(self):
        """Test querying an object from MyModel"""
        start = time.time()
        question_by_problem_id = ChoiceQuestion.objects.filter(problem_id=2)
        
        # my_object = ChoiceQuestion.objects.get()
        # print('xadf')
        print(question_by_problem_id)
        end = time.time()
        print('it takes {} to query'.format(end-start))
        # self.assertEqual(my_object.id, 2)


'''
from .models import Category

class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='Binary Search', weight=1)

    def test_model_can_create_a_category(self):
        cate = Category.objects.get(name='Binary Search')
        self.assertEqual(cate.name, 'Binary Search')
        self.assertEqual(cate.weight, 1)
'''