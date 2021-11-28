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
inv = []
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
    if option == 1:
      print(op1Line[1])
      print(op2Line[1])
    elif option == 2:
      print(op2Line[1])
    else:
      print('invalid')
    print(sLine[3])
    note = 'It said "7/3/01". Those numbers seem familiar, but you cannot remember. It also had an arrow, pointing to your left.'
    print('\n')
    print('You put the note in your inventory. Type inv at an option to print your inventory.')
    inv.append('note: ' + note)
    print('\n')
    oi = input(oLine[2])
    try:
      oi = int(oi)
    except:
      oi == 'inv'
    if oi == 1:
      print(op1Line[2])
      print('\n')
      print(op2Line[2])
    elif oi == 'inv':
      print('\n')
      print(inv)
      oi = input(oLine[2])
      print('\n')
      oi = int(oi)
      if oi == 1:
        print(op1Line[2])
        print('\n')
        print(op2Line[2])
      elif oi == 2:
        print(op2Line[2])
      else:
        print('invalid')
    elif oi == 2:
      print(op2Line[2])
    s.close()
    o.close()
