"""
Recursive algorithms for number representation
"""

def make_binary(length):
    if length == 0:
        return ''

    if length == 1:
        return ['0','1']
    
    res = []
    for i in ['0', '1']:
        for x in make_binary(length - 1):
            res.append(i+x)

    return res

def make_digit_string(length, base):
    if length == 0:
        return ''

    if length == 1:
        return [str(x) for x in range(0,base)]
    
    res = []
    for i in [str(x) for x in range(0,base)]:
        for x in make_digit_string(length - 1, base):
            res.append(i+x)

    return res

def bin_to_dec(bin_num):
    if len(bin_num) == 0:
        return ''

    newNum = 2**(len(bin_num)-1) * int(bin_num[0])

    if len(bin_num) > 1:
        nStr = bin_num[1:]
        newNum += bin_to_dec(nStr)

    return newNum


def val_to_dec(base, num_string):
    vals = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if len(num_string) == 0:
        return ''

    newNum = base**(len(num_string)-1) * vals.find(num_string[0])

    if len(num_string) > 1:
        nStr = num_string[1:]
        newNum += val_to_dec(base,nStr)

    return newNum