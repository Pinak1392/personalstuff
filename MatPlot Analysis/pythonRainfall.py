import csv
from collections import defaultdict
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

#Rainfall 1 handling
x1 = []
y1rain = []
y1temp = []
with open('rainfall1.csv', newline='') as csvfile:
    dictCsv = csv.DictReader(csvfile)
    for i in dictCsv:
        x1.append(int(i['Year']))
        y1rain.append(float(i['Rainfall(mm)']))
        y1temp.append(float(i['Temperature(degrees)']))

x2=[]
y2rain=[]
y2temp=[]
with open('rainfall2.csv', newline='') as csvfile:
    dictCsv = csv.DictReader(csvfile)
    for i in dictCsv:
        x2.append(int(i['Year']))
        y2rain.append(float(i['Rainfall(mm)']))
        y2temp.append(float(i['Temperature(degrees)']))

plt.title('Rain probability density year set 1 vs year set 2')
plt.xlabel('Probability')
plt.ylabel('Rain(mm)')
plt.hist(y1rain, bins=10, density=True, color='b', alpha = 0.5, label='y1 rain histogram')
x = np.linspace(min(y1rain), max(y1rain), 900)
mean = np.average(y1rain)
std = np.std(y1rain)
median = np.median(y1rain)
p = stats.norm.pdf(x, mean, std)
plt.plot(x, p, color='black', label='Normal fit for y1')
print(f'y1rain: mean: {mean}, median: {median}, std: {std}')

plt.hist(y2rain, bins=10, density=True, color='r', alpha = 0.5, label='y2 rain histogram')
x = np.linspace(min(y2rain), max(y2rain), 900)
mean = np.average(y2rain)
std = np.std(y2rain)
median = np.median(y2rain)
p = stats.norm.pdf(x, mean, std)
plt.plot(x, p, color='green', label='Normal fit for y2')
print(f'y2rain: mean: {mean}, median: {median}, std: {std}')

plt.legend()
plt.figure()

plt.title('Temperature probability density year set 1 vs year set 2')
plt.xlabel('Probability')
plt.ylabel('Temperature(degrees)')

plt.hist(y1temp, bins=10, density=True, color='b', alpha = 0.5, label='y1 temp histogram')
x = np.linspace(min(y1temp), max(y1temp), 900)
mean = np.average(y1temp)
std = np.std(y1temp)
median = np.median(y1temp)
p = stats.norm.pdf(x, mean, std)
plt.plot(x, p, color='black', label='Normal fit for y1')
print(f'y1temp: mean: {mean}, median: {median}, std: {std}')

plt.hist(y2temp, bins=10, density=True, color='r', alpha = 0.5, label='y2 temp histogram')
x = np.linspace(min(y2temp), max(y2temp), 900)
mean = np.average(y2temp)
std = np.std(y2temp)
median = np.median(y2temp)
p = stats.norm.pdf(x, mean, std)
plt.plot(x, p, color='green', label='Normal fit for y2')
print(f'y1temp: mean: {mean}, median: {median}, std: {std}')

plt.legend()

plt.figure()
stats.probplot(y1rain, dist='norm', plot=plt)
plt.title('y1 rain qq')

plt.figure()
stats.probplot(y2rain, dist='norm', plot=plt)
plt.title('y2 rain qq')

plt.figure()
stats.probplot(y1temp, dist='norm', plot=plt)
plt.title('y1 temp qq')

plt.figure()
stats.probplot(y2temp, dist='norm', plot=plt)
plt.title('y2 temp qq')

plt.figure()
plt.title('Rain vs Time graph')
plt.xlabel('Time(years)')
plt.ylabel('Rain(mm)')
plt.plot(x1, y1rain, label='year set 1')
plt.plot(x2, y2rain, color='r', label='year set 2')
plt.legend()

plt.figure()
plt.title('Temperature vs Time graph')
plt.xlabel('Time(years)')
plt.ylabel('Temperature(degrees)')
plt.plot(x1, y1temp, label='year set 1')
plt.plot(x2, y2temp, color='r', label='year set 2')
plt.legend()

plt.show()