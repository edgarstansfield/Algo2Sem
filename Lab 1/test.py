import unittest
import shutil

import second, fifth, sixth, thirteenth, fourteenth, seventeenth, twenteth

def cmp_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    for i in range(len(arr1)):
        if arr1[i].strip() != arr2[i].strip():
            return False

    return True

def test(test, task, unittest):
    shutil.copyfile(f'tests/{test}i.txt', 'input.txt')
    task.main()
    with open('output.txt') as output:
        res = output.read().split('\n')
    with open(f'tests/{test}o.txt') as output:
        exp = output.read().split('\n')
    unittest.assertTrue(cmp_arrays(exp, res), 'INCORRECT!')


class Lab1Test(unittest.TestCase):
    def testsecond(self):
        test('2', second, self)
    def testfifth(self):
        test('5', fifth, self)
    def testsixth(self):
        test('6', sixth, self)
    def testthirteenth(self):
        test('13', thirteenth, self)
    def testfourteenth(self):
        test('14', fourteenth, self)
    def testseventeenth(self):
        test('17', seventeenth, self)
    def testtwenteth(self):
        test('20', twenteth, self)


