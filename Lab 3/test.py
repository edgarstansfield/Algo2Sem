import unittest
import shutil

import third, ninth, twelvth, thirteenth

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
    def testthird(self):
        test('3', third, self)
    def testninth(self):
        test('9', ninth, self)
    def testtweltvth(self):
        test('12', twelvth, self)
    def testthirteenth(self):
        test('13', thirteenth, self)


