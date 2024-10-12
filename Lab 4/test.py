import unittest
import shutil

import second, ninth, fifth, eigth

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
    def testeigth(self):
        test('8', eigth, self)
    def testninth(self):
        test('9', ninth, self)


