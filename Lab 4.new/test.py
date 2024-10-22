import unittest
import shutil

from eight import eigth
from second import second
from ninth import ninth
from fifth import fifth


def cmp_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    for i in range(len(arr1)):
        if arr1[i].strip() != arr2[i].strip():
            return False

    return True

def test(direction, test, task, unittest):
    shutil.copyfile(f'{direction}/{test}i.txt', f'{direction}/input.txt')
    task.main()
    with open(f'{direction}/output.txt') as output:
        res = output.read().split('\n')
    with open(f'{direction}/{test}o.txt') as output:
        exp = output.read().split('\n')
    unittest.assertTrue(cmp_arrays(exp, res), 'INCORRECT!')


class Lab1Test(unittest.TestCase):
    def testsecond(self):
        test('second','2', second, self)
    def testfifth(self):
        test('fifth', '5', fifth, self)
    def testeigth(self):
        test('eight','8', eigth, self)
    def testninth(self):
        test('ninth','9', ninth, self)


