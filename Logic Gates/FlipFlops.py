from CombinationGates import *

class Latch(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)
        self.q = 0

    def performGateLogic(self):
        if self.getPinA() == 1 and self.getPinB() == 0:
            self.q = 1
        elif self.getPinA() == 0 and self.getPinB() == 1:
            self.q = 0
        
        return self.q

class JKFlipFlop(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)
        self.qn = 0

    def performGateLogic(self):
        q = self.qn
        if self.getPinA() == 1 and q == 0:
            self.qn = 1
        elif self.getPinB() == 1 and q == 1:
            self.qn = 0
        
        return q


if __name__ == "__main__":
    l1 = JKFlipFlop('G1')
    p1 = Power('P1',0)
    p2 = Power('P2',0)
    c1 = Connector(p1,l1)
    c2 = Connector(p2,l1)
    while True:        
        print(l1.getOutput())
        p1.switch(int(input('Power A: ')))
        p2.switch(int(input('Power B: ')))        