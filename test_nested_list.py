""" Test cases for nested lists file.
"""
import unittest
import nested_lists


class TestNestedLists(unittest.TestCase):
    """ Test cases for nested list function.
    """
    def test_remove_nested_loop_dict(self):
        """ Test case for nested lists passing a dictionary.
        """
        expected = {}
        result = nested_lists.remove_nested_loop(expected)
        self.assertFalse(result)

    def test_remove_nested_loop_list(self):
        """ Test case for nested lists passing a simple list.
        """
        expected = [1, 2, 3, 4]
        result = nested_lists.remove_nested_loop(expected)
        self.assertEqual(result, expected)

    def test_remove_nested_loop_nested_list(self):
        """ Test case for nested lists passing a nested list.
        """
        expected = [1, 2, [3, 4], 5]
        result = nested_lists.remove_nested_loop(expected)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
