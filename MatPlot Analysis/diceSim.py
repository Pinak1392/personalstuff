import random
import matplotlib.pyplot as plt
from itertools import cycle

amount = int(input("amount of dice: "))
maxVal = int(input("max val of dice: "))
trials = int(input("trials: "))

x = []
y = []
exVs = []

for am in range(1, amount+1):
    xVals = [round(i/am, 5) for i in range(1*am, (maxVal * am) + 1)]
    yDict = {}
    for i in xVals:
        yDict[i] = 0

    for i in range(trials):
        val = 0
        for a in range(am):
            val += random.randint(1,maxVal)/am
        
        yDict[round(val, 5)] += 1

    yVals = [yDict[i]/trials for i in xVals]
    exProbs = [xVals[i] * yVals[i] for i in range(len(xVals))]
    exVal = sum(exProbs)
    y.append(yVals)
    x.append(xVals)
    exVs.append(exVal)

for i in range(len(x)):
    plt.plot(x[i], y[i], color=[random.random(),random.random(),random.random()])

plt.xlabel("Value")
plt.ylabel("Probability")
plt.title("IDK WHAT TITLE SHOULD BE")

plt.show()