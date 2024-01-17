import unittest
import exam_modules as test_app

class TestVidssum(unittest.TestCase):
    
    def test_values(self):
        self.assertRaises(ValueError, vidssum, -10000, 6, 17)

    def test_values(self):
        self.assertFalse(TypeError, vidssum, 10000, 6, 'O')
        self.assertFalse(TypeError, vidssum, 10000, 6, True)

if __name__ == '__main__':
    unittest.main()