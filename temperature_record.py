""" TempTracer is class to add temperatures and get minimum, maximum and mean values.
"""


class TempTracer:
    def __init__(self):
        """ Initialization.
        """
        super(TempTracer, self).__init__()
        self.temperature = []

    def insert(self, value):
        """ Function to insert temperature.

            Args:
                value (int): Temperature value.

            Returns:
                bool: Return True if a value is inserted, else return False
        """
        if isinstance(value, int):
            if value in range(0, 110):
                self.temperature.append(value)
                return True
            else:
                return False
        return False

    def get_max(self):
        """ Get maximum temperature of the existing temperature.

            Return:
                int: maximum temperature
        """
        return max(self.temperature)

    def get_min(self):
        """ Get minimum temperature of the existing temperature.

            Return:
                int: minimum temperature
        """
        return min(self.temperature)

    def get_mean(self):
        """ Get mean temperature of the all temperatures.

            Return:
                float: mean temperature
        """
        sum_num = 0
        for temperature in self.temperature:
            sum_num = sum_num + temperature

        # We can remove float for sum_num in python 3 as division in python 3 gives float value.
        avg = float(sum_num) / len(self.temperature)
        return avg
