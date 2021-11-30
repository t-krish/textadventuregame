#text adventure game
import random
import time
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
        inv.append('berries')
      elif oi == 2:
        print(op2Line[2])
      else:
        print('invalid')
    elif oi == 2:
      print(op2Line[2])
    time.sleep(1)
    print('Day')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('Over')
    print(sLine[4])
    oi = input(oLine[3])
    try:
      oi = int(oi)
    except:
      oi == 'inv'
    if oi == 1:
      print(op1Line[3])
    elif oi == 2:
      print("You find a nice cave, but then some \x1B[3mimonsters\x1B[0m drive you out. You go to the other cave")
      print(op1Line[3])
    elif oi == 'inv':
      print(inv)
      if oi == 1:
        print(op1Line[3])
      elif oi == 2:
        print("(You find a nice cave, but then some \x1B[3mmonsters\x1B[0m drive you out. You go to the other cave. )")
        print(op1Line[3])
    print(sLine[5])
    print('\n')
    print(sLine[6])
    print('\n')
    print(sLine[7])
    print('\n')
    #battle system below
    lv = 'No Answer'
    player_health = 100
    enemy_health = 100
    while enemy_health != 0 or player_health != 0: 
      etoa = random.randint(1,2)  
      print('Note: Critical attacks damage yourself.')
      print('\n')
      ptoa = input('What type of attack do you do? Casual, or Critical?')
      #print(ptoa, etoa)
      if etoa == 1 and ptoa == 'casual':
          pd = random.randint(1, 15)
          ed = random.randint(1, 15)
          player_health = player_health - ed
          enemy_health = enemy_health - pd
          print('\n')
          print('Your health: ', player_health, 'and enemy health: ',enemy_health)
      elif etoa == 1 and ptoa == 'critical':
        pd = random.randint(15, 50)
        recoil = random.randint(1, 15)
        ed = random.randint(1, 15)
        #print(recoil,pd,ed)
        player_health = player_health - ed - recoil
        enemy_health = enemy_health - pd
        print('\n')
        print(' You took this much recoil damage:', recoil)
        print('Your health: ', player_health, 'and enemy health: ',enemy_health)
      elif etoa == 2 and ptoa == 'casual':
        pd = random.randint(1, 15)
        ed = random.randint(15, 50)
        recoil = random.randint(1, 15)
        #print(recoil,pd,ed)
        player_health = player_health - ed
        enemy_health = enemy_health - pd - recoil
        print('\n')
        print('Your health: ', player_health, 'and enemy health: ',enemy_health)
      elif etoa == 2 and ptoa == 'critical':
        pd = random.randint(15, 50)
        ed = random.randint(15, 50)
        recoilp = random.randint(1,15)
        recoile = random.randint(1, 15)
        #print(recoilp,recoile,pd,ed)
        player_health = player_health - ed - recoilp
        enemy_health = enemy_health - pd - recoile
        print('\n')
        print(' Your health: ', player_health, 'and enemy health: ',enemy_health)
      if player_health <= 0:
        print('You have been defeated, though you will get another chance.')
        lv = 'loss'
        enemy_health = 100
        player_health = 100
      elif enemy_health <=0:
        print('You win.')
        lv = 'Victory'
        break
      #end of battle
    print('Game complete.')
    print('Goodbye,', name)
    s.close()
    o.close()
    gameStart = 'done'
    