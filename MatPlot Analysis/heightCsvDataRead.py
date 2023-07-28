import csv
from collections import defaultdict
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

Heights = defaultdict(int)
qqHeights = []
rawHeights = []
roundAmt = 2
binWidth = 1/10**roundAmt
mean = 0

with open('HeightWeightData.csv', newline='') as csvfile:
    dictCsv = csv.DictReader(csvfile)

    for i in dictCsv:
        Heights[round(float(i['Height'])/12,roundAmt)] += 1
        qqHeights.append(round(float(i['Height'])/12,roundAmt))
        rawHeights.append(float(i['Height'])/12)

mean = np.mean(rawHeights)
stdTopnotsum = [(i - mean)**2 for i in rawHeights]
variance = sum(stdTopnotsum)/(len(rawHeights) - 1)
std = variance ** (1/2)

print(mean, variance, std, binWidth)

lists = sorted(Heights.items())
x2, y2 = zip(*lists)
y2 = list(y2)
y2sum = sum(y2)
for i in range(len(y2)):
    y2[i] = y2[i]/y2sum

print(sum(y2))

plt.scatter(x2, y2, c='g', label='scatter of heights in bins of 0.01 size')
plt.title('Probability Dist of Heights')

plt.xlabel('Height(feet)')
plt.ylabel('Probability')

xmin = min(rawHeights)
xmax = max(rawHeights)
x = np.linspace(xmin, xmax, 101)
p = stats.norm.pdf(x, mean, std)
plt.plot(x, p*binWidth, 'k', linewidth=2, label='normal fit')
plt.legend()

plt.figure()
stats.probplot(qqHeights, dist="norm", plot=plt)
plt.title('qqPlot of heights dist')

plt.show()