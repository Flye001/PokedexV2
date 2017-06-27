import time
import pygame

pygame.init()
screen = pygame.display.set_mode((800,480))

screen.fill((0,255,0))
#pygame.Surface.fill((2555,0,0))

pygame.display.flip()
time.sleep(5)
pygame.quit()
