import unittest

# 导入待测函数
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

class TestBubbleSort(unittest.TestCase):

    def test_empty_array(self):
        # 测试空数组
        arr = []
        bubble_sort(arr)
        self.assertEqual(arr, [])

    def test_sorted_array(self):
        # 测试已排序的数组
        arr = [1, 2, 3, 4, 5]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        # 测试逆序排列的数组
        arr = [5, 4, 3, 2, 1]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_random_array(self):
        # 测试随机数组
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

if __name__ == '__main__':
    unittest.main()
