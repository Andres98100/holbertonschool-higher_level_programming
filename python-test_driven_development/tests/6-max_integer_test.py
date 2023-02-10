#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    '''unnitest'''
    def test_max_at_the_end(self):
        '''test'''
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_max_at_the_beginning(self):
        '''test'''
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)
    def test_max_in_the_middle(self):
        '''test'''
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

if __name__ == '__main__':
    unittest.main()