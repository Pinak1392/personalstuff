import pygame
from matrix3D import *

pygame.init()

points = [(-1,-1,-1),(1,-1,-1),(-1,1,-1),(-1,-1,1),(1,1,-1),(-1,1,1),(1,-1,1),(1,1,1)]

faces = []
for i in [-1,1]:
    for a in [0,1,2]:
        l = []
        for b in points:
            if b[a] == i:
                l.append(points.index(b))
        faces.append(l)

triangle = []
for i in faces:
    trione = [points[i[0]]]
    tritwo = [points[ind] for ind in i[1:]]
    for a in tritwo:
        diff = 0
        for b in range(len(a)):
            if a[b] != trione[0][b]:
                diff += 1
        
        if diff != 2:
            trione.append(a)
        
    trione = [points.index(i) for i in trione]
    tritwo = [points.index(i) for i in tritwo]
    triangle.append(trione)
    triangle.append(tritwo)

del faces

norms = []
for i in triangle:
    tempTri = []
    for a in range(len(i)):
        tempTri.append(points[i[a]])

    cross = getCross(vectorize(tempTri[0],tempTri[1]),vectorize(tempTri[0],tempTri[2]))
    unitCross = (cross[0]/getDist(cross), cross[1]/getDist(cross), cross[2]/getDist(cross))
    norms.append(unitCross)


# Set up the drawing window

screen = pygame.display.set_mode([600, 600])


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        for i in range(len(points)):
            points[i] = transform([translate(-0.1,0,0)],points[i])
    if keys[pygame.K_RIGHT]:
        for i in range(len(points)):
            points[i] = transform([translate(0.1,0,0)],points[i])
    if keys[pygame.K_UP]:
        for i in range(len(points)):
            points[i] = transform([translate(0,-0.1,0)],points[i])
    if keys[pygame.K_DOWN]:
        for i in range(len(points)):
            points[i] = transform([translate(0,0.1,0)],points[i])
    if keys[pygame.K_w]:
        for i in range(len(points)):
            points[i] = transform([rotateX(0.25)],points[i])
        for i in range(len(norms)):
            norms[i] = transform([rotateX(0.25)],norms[i])
    if keys[pygame.K_s]:
        for i in range(len(points)):
            points[i] = transform([rotateX(-0.25)],points[i])
        for i in range(len(norms)):
            norms[i] = transform([rotateX(-0.25)],norms[i])
    if keys[pygame.K_a]:
        for i in range(len(points)):
            points[i] = transform([rotateY(0.25)],points[i])
        for i in range(len(norms)):
            norms[i] = transform([rotateY(0.25)],norms[i])
    if keys[pygame.K_d]:
        for i in range(len(points)):
            points[i] = transform([rotateY(-0.25)],points[i])
        for i in range(len(norms)):
            norms[i] = transform([rotateY(-0.25)],norms[i])
    if keys[pygame.K_q]:
        for i in range(len(points)):
            points[i] = transform([rotateZ(0.25)],points[i])
        for i in range(len(norms)):
            norms[i] = transform([rotateZ(0.25)],norms[i])
    if keys[pygame.K_e]:
        for i in range(len(points)):
            points[i] = transform([rotateZ(-0.25)],points[i])
        for i in range(len(norms)):
            norms[i] = transform([rotateZ(-0.25)],norms[i])

    screen.fill((0, 0, 0))

    def pointScale(i):
        return (round((i[0] * 100) + 300), round((i[1] * 100) + 300))

    
    zCull = 999
    for i in range(len(triangle)):
        tempTri = []
        tempZ = []
        for a in range(3):
            tempZ.append(points[triangle[i][a]][2])
            tempTri.append(pointScale(points[triangle[i][a]]))

        orientationToPerspective = abs(getDot((0,0,1),norms[i]))

        if orientationToPerspective > 0 and zCull >= min(tempZ):
            zCull = min(tempZ)
            pygame.draw.polygon(screen, (0,255*orientationToPerspective,0), tempTri)

    pygame.display.flip()



pygame.quit()