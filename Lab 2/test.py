import unittest
import shutil

import third, eighth, twelvth, fifteenth, sixteenth

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
    def testeighth(self):
        test('8', eighth, self)
    def testtweltvth(self):
        test('12', twelvth, self)
    def testfifteenth(self):
        test('15', fifteenth, self)
    def testsixteenth(self):
        test('16', sixteenth, self)


