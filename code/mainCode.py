import time
import pygame
import sys

pics = '/home/pi/PokedexV2/pics/'
black = (0,0,0)
pygame.init()
screen = pygame.display.set_mode((800,480))

def startScreen():
	screen.fill(black)
	startScreen = pics+'start-screen.png'
	startScreenPNG = pygame.image.load(startScreen).convert_alpha()
	screen.blit(startScreenPNG, (0,0))
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				mainMenu()

def mainMenu():
	screen.fill(black)
	background = pics+'background.png'
	backgroundPNG = pygame.image.load(background).convert_alpha()
	screen.blit(backgroundPNG, (0,0))
	pygame.display.update()
	
startScreen()
