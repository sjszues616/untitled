"""
题目1:
一个长度为N的整数数组(N>2)，找出其中相乘最大的2个数。
如arr=[1,2,3],则最大值为2X3=6，返回 2,3
只需实现一个函数，函数定义：int fun(Arr){return 相乘最大的2个数;}
"""
import unittest


def get2max(arr):
    if arr[0] < arr[1]:
        temp_1, temp_2 = arr[0], arr[1]
    else:
        temp_2, temp_1 = arr[0], arr[1]
    for i in arr[2:]:
        if i > temp_2:
            temp_2, temp_1 = i, temp_2
        elif i > temp_1:
            temp_1 = i
    return temp_1, temp_2


class Testq1(unittest.TestCase):

    def setUp(self):
        print('开始q1的测试')

    def tearDown(self):
        print('q1的测试结束')

    def test_res(self):
        arr = [1, 2, 3, 12, 3, 4, 1, 4]
        self.assertEqual(get2max(arr),(4,12))


if __name__ == '__main__':
    unittest.main(verbosity=2)