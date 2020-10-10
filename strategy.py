from envelope import Envelope
import random


class BaseStrategy():
    '''
    The Base Strategy class is a the most simple strategy,
    the user choose when to stop.
    '''
    def __init__(self, envelopes):
        self._envelopes = envelopes

    def play(self):
        '''
        The function goes envelope by envelope until the user chooses to stop
        '''
        for i in range(len(self._envelopes)):
            print(self._envelopes[i].money)
            stop = input("Press Y to stop")
            if stop == "Y" or stop == "y":
                print(self._envelopes[i])
                break
            if i == 99:
                print(self._envelopes[i])

    def display(self):
        '''
        Returns the string name of the strategy
        '''
        return "BaseStrategy"


class Automatic_BaseStrategy(BaseStrategy):
    '''
    The Automatic Base Strategy raffles a
    random envelope and this is the chosen one.
    '''
    def __init__(self, envelopes):
        BaseStrategy.__init__(self, envelopes)

    def play(self):
        '''
        The function raffles a random envelope and this is the chosen one
        '''
        rnd = random.randint(0, 99)
        print(self._envelopes[rnd])

    def display(self):
        '''
        Returns the string name of the strategy
        '''
        return "Automatic_BaseStrategy"


class More_then_N_percent_group_strategy(BaseStrategy):
    '''
    The more then N percent group strategy open X% envelopes and search the
    envelopes with the maximum money.After that we search the envelopes that
    remain the first envelopes with the higher amount then the last amount
    '''
    def __init__(self, envelopes, percent=0.25):
        BaseStrategy.__init__(self, envelopes)
        self._percent = percent

    def play(self):
        max = 0
        for i in range(int(self._percent * 100)):
            if(self._envelopes[i].money > max):
                max = self._envelopes[i].money
        for i in range(int(self._percent * 100), len(self._envelopes)):
            if(self._envelopes[i].money > max):
                print(self._envelopes[i])
                return
        print(self._envelopes[len(self._envelopes)-1])

    @property
    def percent(self):
        return self._percent

    @percent.setter
    def percent(self, percent):
        self._percent = percent

    def display(self):
        '''
        Returns the string name of the strategy
        '''
        return "More_then_N_percent_group_strategy"


class N_max_strategy(BaseStrategy):
    def __init__(self, envelopes, N=3):
        BaseStrategy.__init__(self, envelopes)
        self._N = N

    def play(self):
        maxAmount = self._envelopes[0]
        counter = 1
        for i in range(len(self._envelopes)):
            if(self._envelopes[i].money > maxAmount.money):
                maxAmount = self._envelopes[i]
                counter += 1
            if(counter == self._N):
                print(maxAmount)
                return
        print(self._envelopes[-1])

    def display(self):
        '''
        Returns the string name of the strategy
        '''
        return "N_Max_Strategy"

    @property
    def N(self):
        return self._N

    @N.setter
    def N(self, N):
        self._N = N
