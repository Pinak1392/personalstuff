from collections import defaultdict

outputsList = []

outputsDict = {
    'l':['l','l','r','r','r','r','s','s','s','s'],
    'r':['l','l','l','r','r','s','s','s','b','b'],
    's':['l','l','l','l','l','l','l','l','r','b'],
    'b':['l','l','l','l','r','r','r','s','b','b']
}

def recurInter(trials, startMatrix):
    if trials > 1:
        nMat = []
        for i in startMatrix:
            nMat += outputsDict[i]
        
        return recurInter(trials - 1, nMat)
    else:
        return startMatrix

def probDict(l):
    probdict = defaultdict(float)
    for i in l:
        probdict[i] += 1/len(l)

    return probdict

probs = probDict(recurInter(3, ['l','l','l','r','r','r','s','s','s','b']))
print(probs)
print(sum(list(probs.values())))