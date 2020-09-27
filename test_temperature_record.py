"""

"""
import unittest
import temperature_record


class SimpleTest(unittest.TestCase):
    """

    """
    def test_insert_number(self):
        """

        :return:
        """
        value = 12
        temperature = temperature_record.TempTracer()
        result = temperature.insert(value)
        self.assertTrue(result)

    def test_insert_number_range(self):
        """

        :return:
        """
        value = 122
        temperature = temperature_record.TempTracer()
        result = temperature.insert(value)
        self.assertFalse(result)

    def test_insert_string(self):
        value = "String"
        temperature = temperature_record.TempTracer()
        result = temperature.insert(value)
        self.assertFalse(result)

    def test_insert_list(self):
        value = [5, 6, 7]
        temperature = temperature_record.TempTracer()
        result = temperature.insert(value)
        self.assertFalse(result)

    def test_insert_dict(self):
        value = {"value1": 56}
        temperature = temperature_record.TempTracer()
        result = temperature.insert(value)
        self.assertFalse(result)

    def test_insert_empty(self):
        value = None
        temperature = temperature_record.TempTracer()
        result = temperature.insert(value)
        self.assertFalse(result)

    def test_get_max(self):
        temperature = temperature_record.TempTracer()
        temperature.insert(5)
        temperature.insert(10)
        result = temperature.get_max()
        self.assertEqual(result, 10)

    def test_get_min(self):
        temperature = temperature_record.TempTracer()
        temperature.insert(5)
        temperature.insert(10)
        result = temperature.get_min()
        self.assertEqual(result, 5)

    def test_get_mean(self):
        temperature = temperature_record.TempTracer()
        temperature.insert(2)
        temperature.insert(4)
        result = temperature.get_mean()
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
