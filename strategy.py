from envelope import Envelope
import random

class BaseStrategy():

    def __init__(self,envelopes):
        self._envelopes = envelopes

    def play(self):


        for i in range(len(self._envelopes)):
            print(self._envelopes[i].money)
            stop = input("Press Y to stop")
            if stop == "Y":
                return self._envelopes[i]
            if i == 100:
                return self._envelopes[i]

class Automatic_BaseStrategy(BaseStrategy):
    def __init__(self, envelopes):   
        BaseStrategy.__init__(self,envelopes)  
        self._precent = precent

    def play(self):
        rnd = random.randint(0,99)    
        return self._envelopes[rnd]
    

        

class More_then_N_percent_group_strategy(BaseStrategy):
    def __init__(self, envelopes, precent = 0.25):   
        BaseStrategy.__init__(self,envelopes)  
        self._precent = precent

    def play(self):
        max = 0
        for i in range(self._precent*100):
            if(self._envelopes[i].money > max):
                max = self._envelopes[i].money
        for i in range(self._precent*100, len(self._envelopes)):
            if(self._envelopes[i].money > max):
                return self._envelopes[i]
        return self._envelopes[len(self._envelopes)] 


    @property
    def precent(self):
        return self._precent