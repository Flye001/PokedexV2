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
	#define pics
	background = pics+'background.png'
	backgroundPNG = pygame.image.load(background).convert_alpha()
	start = pics+'start.png'
	startPNG = pygame.image.load(start).convert_alpha()
	credits = pics+'credits.png'
	creditsPNG = pygame.image.load(credits).convert_alpha()
	exit = pics+'exit.png'
	exitPNG = pygame.image.load(exit).convert_alpha()
	#blit images
	screen.blit(backgroundPNG, (0,0))
	screen.blit(startPNG, (60,125))
	screen.blit(creditsPNG, (60,246))	#add 121
	screen.blit(exitPNG, (60,367))
	pygame.display.update()
	
startScreen()
