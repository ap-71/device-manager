import random


class GenID:

    @staticmethod
    def gen():
        return int(random.random() * 1000000000000)
