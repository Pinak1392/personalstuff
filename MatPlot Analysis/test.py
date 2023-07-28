import numpy as np
import random

pop = [i for i in range(1,1001)]
out = random.sample(pop,3)
meanPop = np.average(pop)
mean = np.average(out)
std = np.std(out)
rang = f'{meanPop - (2*std)}:{meanPop + (2*std)}'
maxVal = 2*(mean + ((1.96*std)/(3**(1/2)))) - 1
print(maxVal, (maxVal+1)/2, rang, out)