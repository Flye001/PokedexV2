#!/usr/bin/python
#import sys, pygame
#import time
#import subprocess
#import os
#import io
#import socket
#import struct
#import string
poke_number=input("Type your number: ")
pokemon = open('/home/pi/PokedexV2/code/pokemon.csv','r')
content = pokemon.readlines()[poke_number]
id,name=content.split(",")
print name
pokemon.close()
