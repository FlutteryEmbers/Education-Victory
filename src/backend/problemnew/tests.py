from django.test import TestCase
from .models import Problemnew
import time

class MyModelTestCase(TestCase):
    def setUp(self):
        print('start setting up')
        for i in range(10_000_000):
            Problemnew.objects.create(title='sdafgsg', remark= 'dasgdsaf')
        

    def test_query_my_model(self):
        """Test querying an object from MyModel"""
        start = time.time()
        my_object = Problemnew.objects.get(id=2)
        print('xadf')
        print(my_object.id)
        end = time.time()
        print('it takes {} to query'.format(end-start))
        self.assertEqual(my_object.id, 2)