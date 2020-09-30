import random


class Envelope():

    def init(self):
        rnd = random.randint(0,1000)
        self._used = False
        self._money = rnd

    @property
    def money(self):
        self._used = True
        return self._money

    @property
    def used(self):
        return self._used