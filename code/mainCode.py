import time
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,480))

def startScreen():
  startScreen = '/home/pi/PokedexV2/pics/start-screen.png'
  startScreenPNG = pygame.image.load(startScreen).convert_alpha()
  screen.blit(startScreenPNG, (0,0))
  pygame.display.update()
  
  while True:
	  for event in pygame.event.get():
		  if event.type == pygame.MOUSEBUTTONDOWN:
			  sys.exit()

startScreen()
