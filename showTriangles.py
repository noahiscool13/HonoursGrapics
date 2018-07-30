import pygame

from OpenGL.GL import *
from OpenGL.GLU import *

from terrainGen.diamondSquare import diamond_square
from terrainGen.heightmapToTriangles import heightmap_to_triangles

from pygame.locals import *

land = diamond_square([25, 25], 0, 10, 0.5, 1)
water = diamond_square([25, 25], 3, 5, 0.6, 2)

landtriangles = heightmap_to_triangles(land, [-6, -6], [6, 6])
watertriangles = heightmap_to_triangles(water, [-6, -6], [6, 6])


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)
    glEnable(GL_DEPTH_TEST)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[K_LEFT]:
            glRotatef(3, 0, 0, 1)
        if keys_pressed[K_RIGHT]:
            glRotatef(-3, 0, 0, 1)
        if keys_pressed[K_UP]:
            glRotatef(3, 1, 0, 0)
        if keys_pressed[K_DOWN]:
            glRotatef(-3, 1, 0, 0)

        if keys_pressed[K_w]:
            glTranslatef(0, 0.1, 0)
        if keys_pressed[K_s]:
            glTranslatef(0, -0.1, 0)
        if keys_pressed[K_a]:
            glTranslatef(-0.1, 0, 0)
        if keys_pressed[K_d]:
            glTranslatef(0.1, 0, 0)

        if keys_pressed[K_SPACE]:
            glTranslatef(0, 0, -0.2)
        if keys_pressed[K_LSHIFT]:
            glTranslatef(0.0, 0, 0.2)

        # glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glBegin(GL_TRIANGLES)
        for point in landtriangles:
            height = point[2] / 10
            glColor4fv((height, height, height, 1))
            glVertex3fv(point)
        for point in watertriangles:
            height = (point[2] - 3) / 4 + 0.5
            glColor4fv((0.1, 0.1, height, 0.4))
            glVertex3fv(point)
        glEnd()

        pygame.display.flip()
        pygame.time.wait(10)


main()
