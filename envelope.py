import random


class Envelope():

    def init(self):
        rnd = random.randint(0,1000)
        self._amount = rnd

    @property
    def amount(self):
        return self._amount
