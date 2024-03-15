from django.test import TestCase
from .models import Questionnew
from problemnew.models import Problemnew
from utils.tools import Random_Generator, Log
from django.test.utils import CaptureQueriesContext
from django.db import connection
import time

class MyModelTestCase(TestCase):
    def setUp(self):
        print('start setting up')
        self.rg = Random_Generator(seed=10)
        self.log = Log('./new_question_result.txt')
        self.N = 10
        for i in range(self.N):
            problem = Problemnew.objects.create(title=self.rg.sample_one(128), remark=self.rg.sample_one(128))
            question1 = Questionnew.objects.create(problem=problem, type=1, payload=self.rg.generate_random_json(), title=self.rg.sample_one(128))
            question2 = Questionnew.objects.create(problem=problem, type=2, payload=self.rg.generate_random_json(), title=self.rg.sample_one(128))
            question3 = Questionnew.objects.create(problem=problem, type=3, payload=self.rg.generate_random_json(), title=self.rg.sample_one(128))
            question4 = Questionnew.objects.create(problem=problem, type=4, payload=self.rg.generate_random_json(), title=self.rg.sample_one(128))
        

    def test_query_my_model(self):
        """Test querying an object from MyModel"""
        for i in range(10):
            id = self.rg.random_num(self.N)
            with CaptureQueriesContext(connection) as queries:
                problem = Problemnew.objects.get(id=id)
                # Perform the operations that generate queries here
                # print(problem.id)
                item = list(Questionnew.objects.filter(problem_id=problem.id))
                # item2 = Questionnew.objects.filter(problem_id=10, type=2)
            #print(item[0].type)
            # print(queries.captured_queries)
            for query in queries.captured_queries:
                self.log.add_line(f"problem_id:{id}\n" + f"Query: {query['sql']}\n" + f"Duration: {query['time']} seconds\n")
                print(f"Query: {query['sql']}")
                print(f"Duration: {query['time']} seconds")
            
        self.log.dump()