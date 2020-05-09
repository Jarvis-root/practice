import unittest
from Resource import TestFrame



class TestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('------lalalal-------')

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass
