from math import sin, cos, pi

r = pi/180

translate = lambda xt, yt : [[1,0,xt],[0,1,yt],[0,0,1]]
rotate = lambda theta : [[cos(r*theta),-sin(r*theta),0],[sin(r*theta),cos(r*theta),0],[0,0,1]]

def oneDimensionalise(array):
    l = []
    if type(array) == list:
        for i in array:
            l.extend(oneDimensionalise(i))
    else:
        return [array]
    
    return l

def matrixMult(matrix1, matrix2):
    outp = []
    for i in matrix1:
        l = []
        for col in range(len(matrix2[0])):
            val = 0
            for row in range(len(matrix2)):
                val += i[row]*matrix2[row][col]
            l.append(val)
        outp.append(l)
    
    return outp

def transform(transformOrd, coord):
    c = []
    for i in coord:
        c.append([i])
    c.append([1])

    mat = transformOrd[0]
    for i in transformOrd[1:]:
        mat = matrixMult(i, mat)
    
    return tuple(oneDimensionalise(matrixMult(mat, c))[:-1])

def lineEq(pos1, pos2):
    try:
        grad = (pos2[1]-pos1[1])/(pos2[0] - pos1[0])
    except:
        grad = 5000
    inter = pos1[1] - (grad*pos1[0])
    return (grad,inter,pos1[0],pos2[0])

def collision(eq1, eq2):
    try:
        x = (eq1[1] - eq2[1])/(eq2[0] - eq1[0])
    except:
        if eq1[1] == eq2[1]:
            return True
        else:
            return False

    if inbound(eq1[2],x,eq1[3]) and inbound(eq2[2],x,eq2[3]):
        return True
    else:
        return False

def inbound(a,x,b):
    if a <= x and b >= x:
        return True
    elif a >= x and b <= x:
        return True
    else:
        return False