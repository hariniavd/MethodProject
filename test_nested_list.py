"""

"""
import unittest
import nested_lists


class SimpleTest(unittest.TestCase):
    def test_remove_nested_loop_dict(self):
        expected = {}
        result = nested_lists.remove_nested_loop(expected)
        self.assertFalse(result)

    def test_remove_nested_loop_list(self):
        expected = [1, 2, 3, 4]
        nested_lists.remove_nested_loop(expected)
        result = nested_lists.final_list
        self.assertEqual(result, expected)

    def test_remove_nested_loop_nested_list(self):
        expected = [1, 2, [3, 4], 5]
        nested_lists.remove_nested_loop(expected)
        expected = [1, 2, 3, 4, 1, 2, 3, 4, 5]
        result = nested_lists.final_list
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
