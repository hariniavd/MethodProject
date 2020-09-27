"""

"""


class TempTracer:
    def __init__(self):
        super(TempTracer, self).__init__()
        self.temperature = []

    def insert(self, value):
        if isinstance(value, int):
            if value in range(0, 110):
                self.temperature.append(value)
                return True
            else:
                return False
        return False

    def get_max(self):
        return max(self.temperature)

    def get_min(self):
        return min(self.temperature)

    def get_mean(self):
        sum_num = 0
        for temperature in self.temperature:
            sum_num = sum_num + temperature

        avg = sum_num / len(self.temperature)
        return avg
