import unittest
from practice import add_num
from practice import sub_num
from practice import mul_num
from practice import div_num

class MyTest(unittest.TestCase):
    def test1(self):
        self.c = add_num(12,12)
        self.assertEqual(self.c,24)

    def test2(self):
        self.c = sub_num(10,5)
        self.assertEqual(self.c,5)

    def test3(self):
        self.c  = mul_num(5,2)
        self.assertNotEqual(self.c,8)

    def test4(self):
        self.c  = div_num(4,2)
        self.assertNotEqual(self.c,6)

if __name__== '__main__':
    unittest.main()
