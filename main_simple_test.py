import unittest
from main_simple import Anomaly 

class TestStringMethods(unittest.TestCase):
    def test_split(self):
        self.assertEqual(Anomaly([4,6,8,4,3009,12]).anomaly_decision(), [False, False, False, False, True, False])

if __name__ == '__main__':
    unittest.main()