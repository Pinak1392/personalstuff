from math import sin, cos, pi

def vectorize(a,b):
    c = (b[0] - a[0],b[1] - a[1],b[2] - a[2])
    
    return c

def getCross(a,b):
    c = [a[1]*b[2] - a[2]*b[1],
        a[2]*b[0] - a[0]*b[2],
        a[0]*b[1] - a[1]*b[0]]

    return c

def getDot(a,b):
    return (a[0]*b[0]) + (a[1]*b[1]) + (a[2]*b[2])

def getDist(v):
    return ((v[0]**2) + (v[1]**2) + (v[2]**2))**(1/2)

r = pi/180

#Each part list part is a column i.e. the first row of below is |1 0 0 0|
#basically when its the second in a matMult which it always will be its transpose will be used.
translate = lambda xt, yt, zt : [[1,0,0,xt],[0,1,0,yt],[0,0,1,zt],[0,0,0,1]]
rotateX = lambda theta: [[1,0,0,0],[0,cos(r * theta),-sin(r*theta),0],[0,sin(r*theta),cos(r * theta),0],[0,0,0,1]]
rotateY = lambda theta: [[cos(r*theta),0,sin(r * theta),0],[0,1,0,0],[-sin(r*theta),0,cos(r * theta),0],[0,0,0,1]]
rotateZ = lambda theta: [[cos(r * theta),-sin(r*theta),0,0],[sin(r * theta),cos(r*theta),0,0],[0,0,1,0],[0,0,0,1]]

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
            for row in range(len(matrix1)):
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