import unittest
class Feature(object):
    def __init__(self, val):
        self.val = val
    
    def operation(self):
        self.val = self.val**2
        return self.val



class TestClass(unittest.TestCase):
    def test_upper(self):
        obj = Feature(3)
        self.assertEqual(obj.operation(), 9)

if __name__ == '__main__':
    unittest.main()
