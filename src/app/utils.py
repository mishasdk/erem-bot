from random import randint


class Utils:
    @staticmethod
    def choose_random(data):
        return data[randint(0, len(data) - 1)]
