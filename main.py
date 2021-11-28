#text adventure game
import random
import pygame

name = input('What is your name? : ')
start = input('Hello ' + name + ' Please say (start) ').casefold
if start == start:
    gameStart=1
s = open('story.txt', 'r')
sLine = s.readlines()
o = open('options.txt','r')
oLine = o.readlines()
op1 = open('Option1.txt')
op1Line = op1.readlines()
op2 = open('Option2.txt')
op2Line = op2.readlines()
if gameStart == 1:
    print(sLine[0])
    option = input(oLine[0])
    option =int(option)
    if option == 1:
      print(op1Line[0])
    elif option == 2:
      print(op2Line[0])
      print(op1Line[0])
    else:
      print('invalid')
    print(sLine[2])  
    option = input(oLine[1])
    option = int(option)
    s.close()
    o.close()
