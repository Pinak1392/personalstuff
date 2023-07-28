import math
import random

def sig(x):
    return 1/(1 + (math.e)**(-1*x))

def relu(x):
    if x > 0:
        return x
    else:
        return 0

#Remake it