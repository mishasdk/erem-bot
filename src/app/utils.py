from random import randint


class Utils:
    @staticmethod
    def random_from_data(data):
        return data[randint(0, len(data) - 1)]
