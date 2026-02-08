import pygame
import numpy as np
from balls import ball


balls = []

#game settings
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
gravity = 10
speed = 5
hitboxes = []
border = pygame.Rect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():


        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos() # finds mouse when user release click
            mouse_x,mouse_y = mouse_pos
            mouse_pos = np.array([mouse_x,mouse_y],dtype=float)
            balls.append(ball(mouse_pos))
            
            

        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    # RENDER YOUR GAME HERE
    for entity in balls:
        hitboxes.append(entity.hitbox)


    for entity in balls:
        if entity.hitbox.left < 0:
            entity.pos[0] = entity.hitbox.width 
            entity.velocity[0] *= -0.8

        if entity.hitbox.right > SCREEN_WIDTH:
            entity.pos[0] = SCREEN_WIDTH - entity.hitbox.width 
            entity.velocity[0] *= -0.8

        if entity.hitbox.top < 0:
            entity.pos[1] = entity.hitbox.height 
            entity.velocity[1] *= -0.8

        if entity.hitbox.bottom > SCREEN_HEIGHT:
            entity.pos[1] = SCREEN_HEIGHT - entity.hitbox.height 
            entity.velocity[1] *= -0.8  # damping for floor bounce

        
        for other in balls:
            if other is entity:
                continue
            
            if entity.hitbox.colliderect(other.hitbox):
                entity.collide(other)








        entity.hitbox.center = entity.pos

        entity.update_pos()

        entity.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()
    


    clock.tick(60)  # limits FPS to 60

pygame.quit()