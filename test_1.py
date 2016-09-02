import unittest
#
# class TestSequence(unittest.TestCase):
#     def test_3(self): pass
#     def test_2(self): pass
#     def test_1(self): pass
#
# def suite1():
#     suite = unittest.TestSuite()
#     suite.addTest(TestSequence('test_1'))
#     suite.addTest(TestSequence('test_2'))
#
# def suite2():
#     tests = ['test_1', 'test_3']
#     return unittest.TestSuite(map(TestSequence,tests))
#
# suite1 = suite1()
# suite2 = suite2()

class ExpectedFailureCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1,0,'broken')

