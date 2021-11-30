import random
def battle():
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
      print('You have been defeated.')
    elif enemy_health <=0:
      print('You win.')
#all comments were for fixing and checking values