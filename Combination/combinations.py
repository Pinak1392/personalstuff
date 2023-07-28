def combo(sample, amount):
    nli = []
    if amount > 1:
        li = combo(sample,amount-1)
        for x in sample:
            for y in li:
                nli.append([x] + y)
    elif amount == 0:
        return nli
    else:
        for x in sample:
            nli.append([x])

    return nli

def permute(sample, amount):
    nli = []
    if amount > 1:
        li = permute(sample,amount-1)
        for x in sample:
            for y in li:
                if x not in y:
                    nli.append([x] + y)

    elif amount == 0:
        return nli

    else:
        for x in sample:
            nli.append([x])

    return nli

def subsets(sample):
    allSets = set(())
    for x in range(len(sample) + 1):
        a = permute(sample,x)
        for x in a:
            nset = set(())
            for y in x:
                nset.add(y)
            allSets.add(tuple(nset))

    allSets.add(())
    return allSets


if __name__ == "__main__":
    l = [''.join(i) for i in combo(['H','F'],5)]
    print(len(l))