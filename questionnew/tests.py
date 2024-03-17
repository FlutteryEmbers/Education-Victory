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
        self.N = 100_000_000
        self.log = Log('./new_question_result_{}.txt'.format(self.N))
        for i in range(self.N):
            if i % 1000 == 0: print('done create {}'.format(i // 1000))
            problem = Problemnew.objects.create(title=self.rg.sample_one(128), remark=self.rg.sample_one(128))
            question1 = Questionnew.objects.create(problem=problem, type=1, payload=self.rg.generate_random_json(), title=self.rg.sample_one(128))
            question2 = Questionnew.objects.create(problem=problem, type=2, payload=self.rg.generate_random_json(), title=self.rg.sample_one(128))
            question3 = Questionnew.objects.create(problem=problem, type=3, payload=self.rg.generate_random_json(), title=self.rg.sample_one(128))
            question4 = Questionnew.objects.create(problem=problem, type=4, payload=self.rg.generate_random_json(), title=self.rg.sample_one(128))
        

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

    def query_by_id(self, id):
        with CaptureQueriesContext(connection) as queries:
                problem = Problemnew.objects.get(id=id)
                # Perform the operations that generate queries here
                # print(problem.id)
                item = list(Questionnew.objects.filter(problem_id=problem.id))
                # item2 = Questionnew.objects.filter(problem_id=10, type=2)
            #print(item[0].type)
            # print(queries.captured_queries)
        self.log.add_line(f'======test===id{id}==========\n')
        for query in queries.captured_queries:
            self.log.add_line(f"problem_id:{id}\n" + f"Query: {query['sql']}\n" + f"Duration: {query['time']} seconds\n")
            print(f"Query: {query['sql']}")
            print(f"Duration: {query['time']} seconds")

        self.log.add_line(f'================================\n')