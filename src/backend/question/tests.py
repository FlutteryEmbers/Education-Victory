from django.test import TestCase
from .models import ChoiceQuestion, CodingQuestion, TagCoding
from problem.models import Problem
import time
from utils.tools import Random_Generator, Log
from django.test.utils import CaptureQueriesContext
from django.db import connection
import time

class MyModelTestCase(TestCase):
    def setUp(self):
        print('start setting up')
        self.rg = Random_Generator(seed=10)
        self.N = 1_000_000
        self.log = Log('./question_result_{}.txt'.format(self.N))
        for i in range(self.N):
            problem = Problem.objects.create(name=self.rg.sample_one(80))
            question1 = ChoiceQuestion.objects.create(problem=problem, answer_type=0, text_hint=self.rg.sample_one(500))
            question2 = CodingQuestion.objects.create(problem=problem, default_code=self.rg.sample_one(3000), answer=self.rg.sample_one(2000))
            question3 = ChoiceQuestion.objects.create(problem=problem, answer_type=1, text_hint=self.rg.sample_one(500))
        

    def test_query_my_model(self):
        """Test querying an object from MyModel"""
        self.log.add_line(f'======test_random_access==========\n')
        for i in range(100):
            id = self.rg.random_num(self.N)
            self.query_by_id(id=id)

        self.log.add_line(f'======test_access_==========\n')
        ids = [2, self.N//2, self.N - 10]
        for id in ids:
            self.query_by_id(id=id)
        self.log.dump()
        # self.assertEqual(my_object.id, 2)

    def query_by_id(self, id):
        with CaptureQueriesContext(connection) as queries:
            problem = Problem.objects.get(id=id)
            # Perform the operations that generate queries here
            # print(problem.id)
            item = list(ChoiceQuestion.objects.filter(problem_id=problem.id))
            item = list(CodingQuestion.objects.filter(problem_id=problem.id))
            item = list(ChoiceQuestion.objects.filter(problem_id=problem.id))
            # item2 = Questionnew.objects.filter(problem_id=10, type=2)
        #print(item[0].type)
        # print(queries.captured_queries)
        self.log.add_line(f'===========id{id}==========\n')
        for query in queries.captured_queries:
            self.log.add_line(f"problem_id:{id}\n" + f"Query: {query['sql']}\n" + f"Duration: {query['time']} seconds\n")
            print(f"Query: {query['sql']}")
            print(f"Duration: {query['time']} seconds")
        self.log.add_line('================\n')

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