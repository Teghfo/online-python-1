### 1. unittest   2. integrating test
# unittest, pytest, .... 

import unittest
from calculator import Algebra, Calculator


##### AAA testing -----> Arrangement Act Assert


class AlgebraTest(unittest.TestCase):
    def test_generate_algebra(self):
        pass


class CalTest(unittest.TestCase):

    def setUp(self):   # before each test method in this class
        print('setup!')
        self.a = 5
        self.b = 10


    def tearDown(self):  # after each test method in this class
        print('in tearDown')

    @classmethod
    def setUpClass(cls):
        print('setup class')
        cls.cal1= Calculator()


    @classmethod
    def tearDownClass(cls):
        print('tear down class')
        del cls.cal1


    def test_create_obj(self):
        print('in create obj')
        self.assertIsInstance(self.cal1, Calculator)

    def test_suumation(self):
        print('in summation')
        #Arrangement
        

        #Act
        result = self.cal1.summ(self.a,self.b)

        #Assert
        self.assertEqual(result, 15)   # a==b ?
 

    def test_subtraction(self):
        print('in subtraction')


        #Act
        result = self.cal1.subtr(self.a,self.b)

        #Assert
        self.assertEqual(result, -5)   # a==b ?




if __name__ == "__main__":
    unittest.main()
    # assert 10 == 10