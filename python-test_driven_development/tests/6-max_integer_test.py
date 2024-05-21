#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer.py').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_end(self):
        """Test case where the max integer is at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_beginning(self):
        """Test case where the max integer is at the beginning of the list."""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_max_middle(self):
        """Test case where the max integer is somewhere in the middle of the list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_element(self):
        """Test case where the list has only one element."""
        self.assertEqual(max_integer([4]), 4)

    def test_negative(self):
        """Test case where the list contains negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty(self):
        """Test case for an empty list."""
        self.assertIsNone(max_integer([]))

    def test_none(self):
        """Test case where None is passed as the list."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_not_list(self):
        """Test case where a non-list is passed."""
        with self.assertRaises(TypeError):
            max_integer("Hello")

    def test_mixed_types(self):
        """Test case with mixed types within the list."""
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])

if __name__ == '__main__':
    unittest.main()
