import unittest
import add_num

class TestAddNum(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_two_num(self):
        first_num = 1
        sec_num = 2
        result = add_num.add_num(first_num, sec_num)
        self.assertEqual(result, 3)

    def test_third_num(self):
        first_num = 3
        sec_num = 4
        third_num = 5
        result = add_num.add_num(first_num, sec_num, third_num)
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()