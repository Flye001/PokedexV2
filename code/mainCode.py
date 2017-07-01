import time
import pygame
import sys

pics = '/home/pi/PokedexV2/pics/'
black = (0,0,0)
pygame.init()
screen = pygame.display.set_mode((800,480), pygame.FULLSCREEN)

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
	credit = pics+'credits.png'
	creditPNG = pygame.image.load(credit).convert_alpha()
	exit = pics+'exit.png'
	exitPNG = pygame.image.load(exit).convert_alpha()
	#Rect some stuff
	startPos = pygame.Rect(60, 125, 268, 71)
	creditPos = pygame.Rect(60, 246, 268, 71)
	exitPos = pygame.Rect(60, 367, 268, 71)
	#blit images
	screen.blit(backgroundPNG, (0,0))
	screen.blit(startPNG, startPos)
	screen.blit(creditPNG, creditPos)	#image size 268x71 so add 121
	screen.blit(exitPNG, exitPos)
	#display
	pygame.display.update()
	#move Rects
	startPos = startPNG.get_rect()
	startPos = startPos.move(60, 125)
	creditPos = creditPNG.get_rect()
	creditPos = creditPos.move(60, 246)
	exitPos = exitPNG.get_rect()
	exitPos = exitPos.move (60, 367)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = event.pos
				#print mouse_pos
				if startPos.collidepoint(mouse_pos):
					print('Starting...')
					sys.exit()
				if creditPos.collidepoint(mouse_pos):
					print('Credits:')
					sys.exit()
				if exitPos.collidepoint(mouse_pos):
					print('bye')
					sys.exit()
	
startScreen()
