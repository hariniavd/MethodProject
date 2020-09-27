""" Test cases for temperature record class.
"""
import unittest
import temperature_record


class TestTemperatureRecord(unittest.TestCase):
    """ Test case for Temperature record class.
    """
    def test_insert_number(self):
        """ Test case for insert function for number.
        """
        value = 12
        temperature = temperature_record.TempTracer()
        result = temperature.insert(value)
        self.assertTrue(result)

    def test_insert_number_range(self):
        """ Test case for insert function for larger number.
        """
        value = 122
        temperature = temperature_record.TempTracer()
        result = temperature.insert(value)
        self.assertFalse(result)

    def test_insert_string(self):
        """ Test case for insert function for string.
        """
        value = "String"
        temperature = temperature_record.TempTracer()
        result = temperature.insert(value)
        self.assertFalse(result)

    def test_insert_list(self):
        """ Test case for insert function for list.
        """
        value = [5, 6, 7]
        temperature = temperature_record.TempTracer()
        result = temperature.insert(value)
        self.assertFalse(result)

    def test_insert_dict(self):
        """ Test case for insert function for dictonary.
        """
        value = {"value1": 56}
        temperature = temperature_record.TempTracer()
        result = temperature.insert(value)
        self.assertFalse(result)

    def test_insert_empty(self):
        """ Test case for insert function for empty value.
        """
        value = None
        temperature = temperature_record.TempTracer()
        result = temperature.insert(value)
        self.assertFalse(result)

    def test_get_max(self):
        """ Test case for get_max function.
        """
        temperature = temperature_record.TempTracer()
        temperature.insert(5)
        temperature.insert(10)
        result = temperature.get_max()
        self.assertEqual(result, 10)

    def test_get_min(self):
        """ Test case for get_min function.
        """
        temperature = temperature_record.TempTracer()
        temperature.insert(5)
        temperature.insert(10)
        result = temperature.get_min()
        self.assertEqual(result, 5)

    def test_get_mean(self):
        """ Test case for get_mean function.
        """
        temperature = temperature_record.TempTracer()
        temperature.insert(2)
        temperature.insert(4)
        result = temperature.get_mean()
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
