from BasicGates import *

class NandGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        g1 = AndGate(self.getName())
        g1.pinA = self.pinA
        g1.pinB = self.pinB
        g2 = NotGate('G2')
        a = Connector(g1,g2)
        return g2.getOutput()

class NorGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        g1 = OrGate(self.getName())
        g1.pinA = self.pinA
        g1.pinB = self.pinB
        g2 = NotGate('G2')
        a = Connector(g1,g2)
        return g2.getOutput()

class XorGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        g1 = NandGate(self.getName())
        g1.pinA = self.pinA
        g1.pinB = self.pinB

        if g1.pinA == None:
            p1 = Power('P1', g1.getPinA())

        if g1.pinB == None:
            p2 = Power('P2', g1.getPinB())

        g2 = NandGate('G1')
        g3 = NandGate('G2')
        g4 = NandGate('G3')

        if g1.pinA == None:
            a = Connector(p1,g1)
        
        g2.pinA = g1.pinA

        if g1.pinB == None:
            b = Connector(p2,g1)

        g3.pinA = g1.pinB

        e = Connector(g1,g2)
        f = Connector(g1,g3)
        g = Connector(g2,g4)
        h = Connector(g3,g4)

        return g4.getOutput()

class XnorGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        g1 = XorGate(self.getName())
        g1.pinA = self.pinA
        g1.pinB = self.pinB
        g2 = NotGate('G2')
        a = Connector(g1,g2)
        return g2.getOutput()
        
if __name__ == "__main__":
    p1 = Power('P1',1)
    p2 = Power('P2',1)
    g3 = XorGate('G3')
    g1 = NotGate('G1')
    g2 = NotGate('G2')
    cp1 = Connector(p1,g1)
    cp2 = Connector(p2,g2) 
    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)
    print(g3.getOutput())