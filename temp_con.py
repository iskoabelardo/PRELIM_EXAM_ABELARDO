import unittest

def temp_con(a,b,c,d):

    return (a-b)*(c/d)

class Testing(unittest.TestCase):

    def test(self):

        self.assertEqual((32-20)*(5/9),0)

if __name__ == '__main__':

    unittest.main()