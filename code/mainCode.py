import time
import pygame
import sys

pics = '/home/pi/PokedexV2/pics/'

pygame.init()
screen = pygame.display.set_mode((800,480))

def startScreen():
	startScreen = pics+'start-screen.png'
	startScreenPNG = pygame.image.load(startScreen).convert_alpha()
	screen.blit(startScreenPNG, (0,0))
	pygame.display.update()
	while True:
		for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			sys.exit()

def mainMenu():
	background = pics+'background.png'

startScreen()
