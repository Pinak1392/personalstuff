import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random as r

#Contains vertex locations for Cube object
vertices = ((1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,-1),(1,-1,1),(1,1,1),(-1,-1,1),(-1,1,1))

#Defines connections between the vertices. The numbers refer to the element in vertex list.
edges = ((0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,7),(5,4))

faces = ((0,1,2,3),(0,1,4,5),(3,2,7,6),(6,7,5,4),(7,5,1,2),(4,0,3,6))

def set_vertices(max_distance):
    x_change = r.randrange(-10,10)
    y_change = r.randrange(-10,10)
    z_change = r.randrange(-1*max_distance, -20)
    new_vert = []

    #Looks at all vertices and changes them by a random amount and creates a new cube with them
    for vert in vertices:
        nVert = []

        new_x = vert[0] + x_change
        new_y = vert[1] + y_change
        new_z = vert[2] + z_change

        nVert.append(new_x)
        nVert.append(new_y)
        nVert.append(new_z)

        new_vert.append(set(nVert))

    return new_vert


def Cube():
    #Casing for an openGL object where you define certain things.
    glBegin(GL_QUADS)

    #This goes through and draws and connects the dots
    for face in faces:
        glColor3fv((0,1,1))
        for vertex in face:
            glColor3fv((0,1,0))
            glVertex3fv(vertices[vertex])
            

    glEnd()

    #Casing for an openGL object where you define certain things.
    glBegin(GL_LINES)

    #This goes through and draws and connects the dots
    for edge in edges:
        glColor3fv((1,1,0))
        for vertex in edge:
            glColor3fv((0,1,0))
            glVertex3fv(vertices[vertex])

    glEnd()

if __name__ == '__main__':
    pygame.init()
    display = (800,600)

    #Must set openGL stuff in pygame display
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    '''Sets perspective. This is currently 45 degrees. The second parameter is the aspect ratio.
        The third and fourth parameter define how close and how far before the object will stop showing.'''
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    #Allows cube to repeat 10 times.
    for x in range(10):        
        #The x y z coordinates of the perspective or camera 
        glTranslatef(0.0,0.0,-40.0)

        #The camera rotate#
        # glRotatef(0,0,0,0)

        o_pass = False

        while not o_pass:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                            glTranslatef(0.5,0,0)
                    if event.key == pygame.K_RIGHT:
                            glTranslatef(-0.5,0,0) 
                    if event.key == pygame.K_DOWN:
                            glTranslatef(0,1,0) 
                    if event.key == pygame.K_UP:
                            glTranslatef(0,-1,0) 
                
                #Code for mouse scroll
                '''if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        glTranslatef(0,0,0.5)
                    if event.button == 5:
                        glTranslatef(0,0,-0.5)'''


            #Gets your camera pos
            camPos = glGetDoublev(GL_MODELVIEW_MATRIX)

            camX = camPos[3][0]
            camY = camPos[3][1]
            camZ = camPos[3][2]

            if camZ < 0:
                o_pass = True

            #Tells OpenGl what to clear of screen
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

            glTranslatef(0,0,0.5) 
            Cube()
            
            pygame.display.flip()
            pygame.time.wait(50)
