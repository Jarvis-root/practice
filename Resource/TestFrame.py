import unittest


class TestFrame(unittest.TestCase):
    def __init__(self):
        super(TestFrame, self).__init__(methodName='run')
        self.result = 'pass'
        self.test_fail_flag = False

    def Prepare(self):
        pass

    def Procedore(self):
        pass

    def Cleanup(self):
        pass

    def setUp(self):
        self.Prepare()

    def run(self):
        self.Procedore()

    def tearDown(self):
        self.Cleanup()


