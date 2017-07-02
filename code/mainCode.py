import time
import pygame
import sys
import os

pics = '/home/pi/PokedexV2/pics/'
black = (0,0,0)
pygame.init()
screen = pygame.display.set_mode((800,480), pygame.FULLSCREEN)
#back = pics+'back.png'
#backPNG = pygame.image.load(back).convert_alpha()
#backPos = pygame.Rect(60, 367, 268, 71)

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
					startMenu()
				if creditPos.collidepoint(mouse_pos):
					print('Credits:')
					sys.exit()
				if exitPos.collidepoint(mouse_pos):
					exitMenu()

def startMenu():
	screen.fill(black)
	#define pics
	background = pics+'background.png'
	backgroundPNG = pygame.image.load(background).convert_alpha()
	pokedex = pics+'Pokedex.png'
	pokedexPNG = pygame.image.load(pokedex).convert_alpha()
	camera = pics+'camera.png'
	cameraPNG = pygame.image.load(camera).convert_alpha()
	back = pics+'back.png'
	backPNG = pygame.image.load(back).convert_alpha()
	#Rect some stuff
	pokedexPos = pygame.Rect(60, 125, 268, 71)
	cameraPos = pygame.Rect(60, 246, 268, 71)
	backPos = pygame.Rect(60, 367, 268, 71)
	#blit images
	screen.blit(backgroundPNG, (0,0))
	screen.blit(pokedexPNG, pokedexPos)
	screen.blit(cameraPNG, cameraPos)
	screen.blit(backPNG, backPos)
	#display
	pygame.display.update()
	#move Rects
	pokedexPos = pokedexPNG.get_rect()
	pokedexPos = pokedexPos.move(60, 125)
	cameraPos = cameraPNG.get_rect()
	cameraPos = cameraPos.move(60, 246)
	backPos = backPNG.get_rect()
	backPos = backPos.move(60, 367)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = event.pos
				if pokedexPos.collidepoint(mouse_pos):
					pokedexMenu()
				if cameraPos.collidepoint(mouse_pos):
					print('Camera GO!!!')
					sys.exit()
				if backPos.collidepoint(mouse_pos):
					mainMenu()

def exitMenu():
	screen.fill(black)
	#define pics
	background = pics+'background.png'
	backgroundPNG = pygame.image.load(background)
	exit = pics+'exit.png'
	exitPNG = pygame.image.load(exit).convert_alpha()
	shutdown = pics+'shutdown.png'
	shutdownPNG = pygame.image.load(shutdown).convert_alpha()
	back = pics+'back.png'
	backPNG = pygame.image.load(back).convert_alpha()
	#Rect some stuff
	exitPos = pygame.Rect(60, 125, 268, 71)
        shutdownPos = pygame.Rect(60, 246, 268, 71)
        backPos = pygame.Rect(60, 367, 268, 71)
	#blit images
	screen.blit(backgroundPNG, (0,0))
	screen.blit(exitPNG, exitPos)
	screen.blit(shutdownPNG, shutdownPos)
	screen.blit(backPNG, backPos)
	#display
	pygame.display.update()
	#move Rects
	exitPos = exitPNG.get_rect()
	exitPos = exitPos.move(60, 125)
	shutdownPos = shutdownPNG.get_rect()
	shutdownPos = shutdownPos.move(60, 246)
	backPos = backPNG.get_rect()
	backPos = backPos.move(60, 367)
	while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                mouse_pos = event.pos
				if exitPos.collidepoint(mouse_pos):
					sys.exit()
				if shutdownPos.collidepoint(mouse_pos):
					os.system('shutdown now')
				if backPos.collidepoint(mouse_pos):
					mainMenu()
					
def pokedexMenu():
	screen.fill(black)
	#define pics
	background = pics+'background.png'
	backgroundPNG = pygame.image.load(background).convert_alpha()
	database = pics+'database.png'
	databasePNG = pygame.image.load(database).convert_alpha()
	search = pics+'search.png'
	searchPNG = pygame.image.load(search).convert_alpha()
	back = pics+'back.png'
	backPNG = pygame.image.load(back).convert_alpha()
	#Rect some stuff
	databasePos = pygame.Rect(60, 125, 268, 71)
	searchPos = pygame.Rect(60, 246, 268, 71)
	backPos = pygame.Rect(60, 367, 268, 71)
	#blit images
	screen.blit(backgroundPNG, (0,0))
	screen.blit(databasePNG, databasePos)
	screen.blit(searchPNG, searchPos)
	screen.blit(backPNG, backPos)
	#display
	pygame.display.update()
	#move Rects
	databasePos = databasePNG.get_rect()
	databasePos = databasePos.move(60, 125)
	searchPos = searchPNG.get_rect()
	searchPos = searchPos.move(60, 246)
	backPos = backPNG.get_rect()
	backPos = backPos.move(60, 367)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = event.pos
				if databasePos.collidepoint(mouse_pos):
					databaseMenu()
				if searchPos.collidepoint(mouse_pos):
					print('Searching...')
					sys.exit()
				if backPos.collidepoint(mouse_pos):
					startMenu()

def databaseMenu():
	screen.fill(black)
	#define pics
	background = pics+'background.png'
	backgroundPNG = pygame.image.load(background).convert_alpha()
	up = pics+'back.png'
	upPNG = pygame.image.load(up).convert_alpha()
	down = pics+'back.png'
	downPNG = pygame.image.load(down).convert_alpha()
	back = pics+'back.png'
	backPNG = pygame.image.load(back).convert_alpha()
	#Rect some stuff
	upPos = pygame.Rect(60, 125, 268, 71)
	downPos = pygame.Rect(60, 246, 268, 71)
	backPos = pygame.Rect(60, 367, 268, 71)
	#blit images
	screen.blit(backgroundPNG,(0,0))
	screen.blit(upPNG, upPos)
	screen.blit(downPNG, downPos)
	screen.blit(backPNG, backPos)
	#display
	pygame.display.update()
	#move Rects
	upPos = upPNG.get_rect()
        upPos = upPos.move(60, 125)
        downPos = downPNG.get_rect()
        downPos = downPos.move(60, 246)
        backPos = backPNG.get_rect()
        backPos = backPos.move (60, 367)
	pokeNum = 1
	pokeMax = 5 #Maximum pokemon number
	while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                mouse_pos = event.pos
                                if upPos.collidepoint(mouse_pos):
					pokeNum = pokeNum+1
					if pokeNum > pokeMax:
						pokeNum = 1
					pokeStr = str(pokeNum)
					pokeLength = len(pokeStr)
					if pokeLength == 1:
						pokeStr = "00" + pokeStr
					if pokeLength == 2:
						pokeStr = "0" + pokeStr
					print pokeStr
					print pokeNum
	

                                if downPos.collidepoint(mouse_pos):
                                        pokeNum = pokeNum-1
					if pokeNum ==0:
						pokeNum = pokeMax
					pokeStr = str(pokeNum)
                                        pokeLength = len(pokeStr)
                                        if pokeLength == 1:
                                                pokeStr = "00" + pokeStr
                                        if pokeLength == 2:
                                                pokeStr = "0" + pokeStr
                                        print pokeStr
					print pokeNum
				
                                if backPos.collidepoint(mouse_pos):
                                        pokedexMenu()

startScreen()
