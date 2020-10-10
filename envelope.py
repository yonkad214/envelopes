from random import randint


class Envelope():

    def __init__(self):
        rnd = randint(0,1000)
        self._used = False
        self._money = rnd

    def __str__(self):
        return "Money: " + str(self._money)

    @property
    def money(self):
        self._used = True
        return self._money

    @property
    def used(self):
        return self._used
