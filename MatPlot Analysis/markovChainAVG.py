import random
import numpy as np

A = [0.2,0.4,0.4,0]
B = [0.3,0.2,0.3,0.2]
C = [0.8,0.1,0,0.2]
D = [0.4,0.3,0.1,0.2]

predictedAvg = [(A[i] + B[i] + C[i] + D[i])/4 for i in range(4)]

init = [0.1,0.9,0,0]

trials = 1000000
sets = 1

probsOfA = []
probsOfB = []
probsOfC = []
probsOfD = []
for i in range(sets):
    probA = 0
    probB = 0
    probC = 0
    probD = 0
    for i in range(trials):
        l = []
        for a in range(len(init)):
            for b in range(int(10*init[a])):
                l.append(a)

        choice = random.choice(l)

        if choice == 0:
            probA += 1/trials
            init = A
        elif choice == 1:
            probB += 1/trials
            init = B
        elif choice == 2:
            probC += 1/trials
            init = C
        elif choice == 3:
            probD += 1/trials
            init = D
    
    probsOfA.append(probA)
    probsOfB.append(probB)
    probsOfC.append(probC)
    probsOfD.append(probD)

print(np.average(probsOfA),np.average(probsOfB),np.average(probsOfC),np.average(probsOfD))
print(predictedAvg)