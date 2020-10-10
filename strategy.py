from envelope import Envelope

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

class N_max_strategy(BaseStrategy):
    def __init__(self, envelopes, N):
        BaseStrategy.__init__(self, envelopes)
        self.N = N

    def play(self, N):
        maxAmount = self._envelopes[0]
        counter = 1;
        for i in range (len(self._envelopes)):
            if(self._envelopes[i] > max):
                maxAmount = self._envelopes[i]
                counter += 1
            if(counter == N):
                break
        return maxAmount
