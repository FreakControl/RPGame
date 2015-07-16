#!/usr/bin/python
import random
import os
import sys
import time
class Game():
 def __init__(self):
  self.ClearScreen()
  new=int(raw_input('Are you new? (1=yes 0=no): ')) #new?
  if new==1:
   self.playerName=raw_input('Username: ') #pussydestroyer
   self.potionsLeft=3
   self.playerHealth=100
   self.playerMaxHealth=100
   self.playerLevel=1
   self.playerXP=0
   self.playerNextLevelXP=300
   self.GP=0
   self.playerWeapon='melee:Sword:0:5'
   self.playerArmor='clothes:1.0'
   self.playerArmorClass=float(self.playerArmor.split(':')[1])
   self.playerHealthPotion='lesser:25:3'
   self.Location='town hall'
   self.goblinsKilled=0
   self.orcsKilled=0
   print 'Welcome to RPGame! Thanks for playing!' #thanks!
  else:
   self.savedGame(raw_input('Save File: '), 'load')
  while 1:
   self.checkLocation(self.Location)
 def ClearScreen(self):
  if sys.platform=="windows":
   print os.popen("cls").read()
  else:
   print os.popen("clear").read()
 def savedGame(self, savefile, mode):
  encryptedSaveData=''
  decryptedSaveData=''
  key=ord('!')
  if mode=='save':
   print 'Saving game...'
   saveData='''self.playerName="'''+self.playerName+'''"
self.playerHealth=float('''+str(self.playerHealth)+''')
self.playerMaxHealth='''+str(self.playerMaxHealth)+'''
self.playerLevel='''+str(self.playerLevel)+'''
self.playerXP='''+str(self.playerXP)+'''
self.playerNextLevelXP='''+str(self.playerLevel*300*2)+'''
self.GP='''+str(self.GP)+'''
self.playerWeapon="'''+self.playerWeapon+'''"
self.playerArmor="'''+self.playerArmor+'''"
self.playerArmorClass=float('''+str(self.playerArmorClass)+''')
self.playerHealthPotion="'''+self.playerHealthPotion.split(":")[0]+":"+self.playerHealthPotion.split(":")[1]+":"+str(self.potionsLeft)+'''"
self.Location="'''+self.Location+'''"
self.goblinsKilled='''+str(self.goblinsKilled)+'''
self.orcsKilled='''+str(self.orcsKilled)
   for x in saveData:
    encryptedSaveData+=chr(key^ord(x))
   f=open(savefile+'.save', 'wb')
   f.write(encryptedSaveData)
  elif mode=='load':
   print 'Loading game...'
   f=open(savefile+'.save', 'rb')
   saveData=f.read()
   for x in saveData:
    decryptedSaveData+=chr(key^ord(x))
   try:
    exec(decryptedSaveData)
    print 'Welcome back '+self.playerName+'!!!'
   except:
    print 'Save file corrupt.'
    exit(1)
 def battleEnemy(self, enemyName, enemyGender, enemyHealth, enemyDamage, enemyLevel, enemyWeapon, enemyWeaponType, enemyArmorClass):
  print 'Level '+str(enemyLevel)+' '+enemyName+' has appeared.'
  print '1. Fight.'
  print '2. Run.'
  if raw_input('> ')=='1':
   self.ClearScreen()
   weaponType=self.playerWeapon.split(':')[0]
   playerWeaponName=self.playerWeapon.split(':')[1]
   playerDamage=int(self.playerWeapon.split(':')[3])
   potionType=str(self.playerHealthPotion.split(':')[0])
   potionHealing=int(self.playerHealthPotion.split(':')[1])
   self.potionsLeft=int(self.playerHealthPotion.split(':')[2])
   enemyMaxHealth=enemyHealth
   if enemyGender:
    enemyGender='his'
   else:
    enemyGender='her'
   if weaponType=='melee':
    action='swung'
   elif weaponType=='ranged':
    action='shot'
   elif weaponType=='magic':
    action='cast'
   if enemyWeaponType=='melee':
    enemyAction='swung'
   elif enemyWeaponType=='ranged':
    enemyAction='shot'
   elif enemyWeaponType=='magic':
    enemyAction='cast'
   if enemyWeaponType=='melee':
    if weaponType=='melee':
     playerTotalDamage=playerDamage*enemyArmorClass
    elif weaponType=='ranged':
     playerTotalDamage=playerDamage*enemyArmorClass*0.75
    elif weaponType=='magic':
     playerTotalDamage=playerDamage*enemyArmorClass*1.25
   elif enemyWeaponType=='ranged':
    if weaponType=='melee':
     playerTotalDamage=playerDamage*enemyArmorClass*1.25
    elif weaponType=='ranged':
     playerTotalDamage=playerDamage*enemyArmorClass
    elif weaponType=='magic':
     playerTotalDamage=playerDamage*enemyArmorClass*0.75
   elif enemyWeaponType=='magic':
    if weaponType=='melee':
     playerTotalDamage=playerDamage*enemyArmorClass*0.75
    elif weaponType=='ranged':
     playerTotalDamage=playerDamage*enemyArmorClass*1.25
    elif weaponType=='Magic':
     playerTotalDamage=playerDamage*enemyArmorClass
   if weaponType=='melee':
    if enemyWeaponType=='melee':
     totalEnemyDamage=enemyDamage*self.playerArmorClass
    elif enemyWeaponType=='ranged':
     totalEnemyDamage=enemyDamage*self.playerArmorClass*1.25
    elif enemyWeaponType=='magic':
     totalEnemyDamage=enemyDamage*self.playerArmorClass*0.75
   elif weaponType=='ranged':
    if enemyWeaponType=='melee':
     totalEnemyDamage=enemyDamage*self.playerArmorClass*0.75
    elif enemyWeaponType=='ranged':
     totalEnemyDamage=enemyDamage*self.playerArmorClass
    elif enemyWeaponType=='magic':
      totalEnemyDamage=enemyDamage*self.playerArmorClass*1.25
   elif weaponType=='magic':
    if enemyWeaponType=='melee':
     totalEnemyDamage=enemyDamage*self.playerArmorClass*1.25
    elif enemyWeaponType=='ranged':
     totalEnemyDamage=enemyDamage*self.playerArmorClass*0.75
    elif enemyWeaponType=='magic':
     totalEnemyDamage=enemyDamage*self.playerArmorClass
   while 1:
    print '1. Attack using '+playerWeaponName+' ('+str(playerDamage)+' damage).'
    print '2. Use '+potionType+' health potion (heals '+str(potionHealing)+',  '+str(self.potionsLeft)+' potions remaining.)'
    print
    if raw_input('> ')=='1':
     self.ClearScreen()
     enemyHealth-=playerDamage*enemyArmorClass
     print
     print 'You **'+action+'** your '+playerWeaponName+' at the '+enemyName+' for '+str(playerTotalDamage)+' '+weaponType+' damage.'
     print
     print 'Enemy has '+str(enemyHealth)+'/'+str(enemyMaxHealth)+' health remaining.'
     print
     if enemyHealth<=0:
      print 'Level '+str(enemyLevel)+' '+enemyName+' has died!'
      return True
      break
     time.sleep(random.randrange(1,10))
     self.ClearScreen()
     self.playerHealth-=totalEnemyDamage
     print
     print 'Level '+str(enemyLevel)+' '+enemyName+' **'+enemyAction+'** '+enemyGender+' '+enemyWeapon+' at you for '+str(totalEnemyDamage)+' '+weaponType+' damage.'
     print
     print 'You have '+str(self.playerHealth)+'/'+str(self.playerMaxHealth)+' health remaining.'
     print
     if self.playerHealth<=0:
      print 'You were killed by a level '+str(enemyLevel)+' '+enemyName+'.' #straightup beatup
      exit()
    else:
     self.ClearScreen()
     if self.potionsLeft>=1 and self.playerHealth!=self.playerMaxHealth:
      self.potionsLeft-=1
      self.playerHealth+=potionHealing
      if potionType=='UBER':
       self.playerMaxHealth+=10
      if self.playerHealth>=self.playerMaxHealth:
       self.playerHealth=self.playerMaxHealth
      print
      print 'You drank a '+potionType+' healing potion. (+'+str(potionHealing)+' health).'
      print
      print 'You have '+str(self.playerHealth)+'/'+str(self.playerMaxHealth)+' health remaining.'
      print
  else:
   self.ClearScreen()
   insults = ["Pussy.","Sissy.","Coward.","Loser.","Slacker.","We all know you'll just run into another monster eventually."]
   print random.choice(insults)
   return False
 def checkLocation(self, location):
  self.ClearScreen()
  if location=='town hall':
   print 'You find yourself in town hall'
   print '1. Talk to mayor.'
   print '2. Save game.'
   print '3. leave to town square.'
   a=raw_input('> ')
   self.ClearScreen()
   if a=='1':
    print 'Say:'
    print '1. Talk to him about the '+str(self.goblinsKilled)+' goblins you killed.'
    print '2. Talk to him about the '+str(self.orcsKilled)+' orcs you killed.'
    a=raw_input('> ')
    self.ClearScreen()
    if a=='1':
     print 'You talk to him about the '+str(self.goblinsKilled)+' goblins you killed.'
     if self.goblinsKilled<=1:
      print 'But he seems to be occupied.'
     else:
      print 'The mayor happily gives you '+str(self.goblinsKilled*250)+' GP as reward.'
      self.GP+=self.goblinsKilled*250
      self.goblinsKilled=0
    elif a=='2':
     print 'You talk to him about the '+str(self.orcsKilled)+' orcs you killed.'
     if self.orcsKilled<=1:
      print 'But he appears busy doing paperwork.'
     else:
      print 'The mayor smiles and happily gives you '+str(self.orcsKilled*500)+' GP as reward.'
      self.GP+=self.orcsKilled*500
      self.orcsKilled=0
   elif a=='2':
    self.savedGame(raw_input('Save name: '), 'save')
   elif a=='3':
    location='town square'
  if location=='town square':
   print 'You arrive in the town square.'
   print '1. Talk to merchant.'
   print '2. Talk to wounded knight.'
   print '3. Leave to forest.'
   print '4. Go to town hall.'
   b=raw_input('> ')
   self.ClearScreen()
   if b=='1':
    while 1:
     print 'You currently have '+str(self.GP)+' GP left.'
     print '1. Buy melee weapons.'
     print '2. Buy ranged weapons.'
     print '3. Buy magic weapons.'
     print '4. Buy health potions.'
     print '5. Back.'
     print 'Note: all weapons bought will replace your current weapon.'
     print 'also,  you can only hold one type of potion at a time.'
     b=raw_input('> ')
     self.ClearScreen()
     if b=='1':
      print 'Melee weapons have a bonus to damage against archers (1.25x) but do less damage against mages (0.75x).'
      print '1. Buy common rapier, 15 damage. 3000 GP'
      print '2. Buy uncommon broadsword, 25 damage. 5000 GP.'
      print '3. Buy rare diamond sword, 50 damage. 10000 GP.'
      print '4. Buy very rare diamond claymore, 100 damage. 20000 GP.'
      print '5. Buy LEGENDARY adamantium sword, ???? damage 999999 GP.'
      print '6. Back.'
      a=raw_input('> ')
      self.ClearScreen()
      if a=='1':
       if self.GP-3000<0:
        print "You don't have enough money for that!"
       else:
        self.GP-=3000
        print 'You bought the rapier for 3000 GP.'
        self.playerWeapon='melee:rapier:5:15'
      elif a=='2':
       if self.GP-5000<0:
        print "You don't have enough money for that!"
       else:
        self.GP-=5000
        print 'You bought the broadsword for 5000 GP.'
        self.playerWeapon='melee:broadsword:4:25'
      elif a=='3':
        if self.GP-1000<0:
         print "You don't have enough money for that!"
        else:
         self.GP-=10000
         print 'You bought the diamond sword for 10000 GP.'
         self.playerWeapon='melee:diamond sword:3:50'
      elif a=='4':
       if self.GP-20000<0:
        print "You don't have enough money for that!"
       else:
        self.GP-=20000
        print 'You bought the diamond claymore for 20000 GP.'
        self.playerWeapon='melee:diamond claymore:2:100'
      elif a=='5':
       if self.GP-999999<0:
        print "You don't have enough money for that!"
       else:
        self.GP-=999999
        self.playerWeapon='melee:adamantium sword:1:9999'
        print 'You either hacked it (good job!), or you are serously addicted. weirdo.'
        print 'Anyway, have your sword. pff.'
      elif b=='6':
       self.checkLocation(location)
     elif b=='2':
      print 'Ranged weapons have a bonus to damage against mages (1.25x) but do less damage against knights (0.75x).'
      print '1. Buy common short bow, 25 damage. 5000 GP'
      print '2. Buy common bow, 50 damage. 7500 GP'
      print '3. Buy uncommon long bow, 100 damage, 15000 GP.'
      print '4. Buy rare composite bow, 150 damage, 30000 GP.'
      a=raw_input('> ')
      self.ClearScreen()
      if a=='1':
       if self.GP-5000<0:
        print "You don't have enough money for that!"
       else:
        self.GP-=5000
        print 'You bought the short bow for 5000 GP.'
        self.playerWeapon='ranged:short bow:5:25'
      elif a=='2':
       if self.GP-7500<0:
        print "You don't have enough money for that!"
       else:
        self.GP-=7500
        print 'You bought the bow for 7500 GP.'
        self.playerWeapon='ranged:bow:5:50'
      elif a=='3':
       if self.GP-15000<0:
        print "You don't have enough money for that!"
       else:
        self.GP-=15000
        print 'You bought the long bow for 15000 GP.'
        self.playerWeapon='ranged:long bow:4:100'
      elif a=='4':
       if self.GP-30000<0:
        print "You don't have enough money for that!"
       else:
        self.GP-=30000
        print 'You bought the composite bow for 30000 GP.'
        self.playerWeapon='ranged:composite bow:4:150'
      elif b=='5':
       self.checkLocation(location)
     elif b=='3':
      print 'Magic weapons have a bonus to damage against kights (1.25x) but do less damage against archers (0.75x).'
      print '1. Buy (common) fire bolt,  25 damage. 5000 self.GP'
      print '2. Buy (common) air strike,  50 damage. 7500 self.GP'
      print '3. Buy (uncommon) elemental ray,  100 damage,  15000 GP.'
      print '4. Buy (rare) ray of scorching,  150 damage,  30000 GP.'
      a=raw_input('> ')
      self.ClearScreen()
      if a=='1':
       if self.GP-5000<0:
        print "You don't have enough money for that!"
       else:
        self.GP-=5000
        print 'You bought fire bolt for 5000 GP.'
        self.playerWeapon='magic:fire bolt:5:25'
      elif a=='2':
       if self.GP-7500<0:
        print "You don't have enough money for that!"
       else:
        self.GP-=7500
        print 'You bought air strike for 7500 GP.'
        self.playerWeapon='magic:air strike:5:50'
      elif a=='3':
       if self.GP-15000<0:
        print "You don't have enough money for that!"
       else:
        self.GP-=15000
        print 'You bought elemental ray for 15000 GP.'
        self.playerWeapon='magic:elemental ray:4:100'
      elif a=='4':
       if self.GP-30000<0:
        print "You don't have enough money for that!"
       else:
        self.GP-=30000
        print 'You bought ray of scorching for 30000 GP.'
        self.playerWeapon='magic:ray of scorching:3:150'
      elif b=='5':
       self.checkLocation(location)
     elif b=='4':
      print '1. Buy lesser health potion,  heals 25. 25 self.GP. {Bestseller!}'
      print '2. Buy normal health potion,  heals 50. 100 GP.'
      print '3. Buy greater health potion,  heals 100. 150 GP.'
      print '4. But UBER health potion,  heals fully and increases max health by 10. 1000 self.GP'
      print '5. Exit to town square.'
      a=raw_input('> ')
      self.ClearScreen()
      if a=='1':
       if self.GP-25<=0:
        print "You don't have enough money for that!"
       else:
        self.GP-=25
        print 'You bought a lesser health potion for 25 GP.'
        if self.playerHealthPotion.split(':')[0]=='normal':
         currentAmount=int(self.playerHealthPotion.split(':')[2])
        else:
         currentAmount=0
        self.playerHealthPotion='lesser:25:'+str(int(currentAmount+1))
      elif a=='2':
       if self.GP-50<=0:
        print "You don't have enough money for that."
       else:
        self.GP-=50
        print 'You bought a normal health potion for 75 GP.'
        if self.playerHealthPotion.split(':')[0]=='normal':
         currentAmount=int(self.playerHealthPotion.split(':')[2])
        else:
         currentAmount=0
        self.playerHealthPotion='normal:50:'+str(int(currentAmount+1))
      elif a=='3':
       if self.GP-150<=0:
        print "You don't have enough money for that."
       else:
        self.GP-=150
        print 'You bought a greater health potion for 150 GP.'
        if self.playerHealthPotion.split(':')[0]=='greater':
         currentAmount=int(self.playerHealthPotion.split(':')[2])
        else:
         currentAmount=0
        self.playerHealthPotion='greater:100:'+str(int(currentAmount+1))
      elif a=='4':
       if self.GP-1000<=0:
        print "You don't have enough money for that."
       else:
        self.GP-=1000
        print 'You bought an UBER health potion for 1000 GP.'
        if self.playerHealthPotion.split(':')[0]=='UBER':
         currentAmount=int(self.playerHealthPotion.split(':')[2])
        else:
         currentAmount=0
        self.playerHealthPotion='UBER:9999:'+str(int(currentAmount+1))
     elif b=='5':
      self.checkLocation(location)
    self.checkLocation(location)
   elif b=='2':
    print '1. Ask what happened.'
    print '2. Ask about other raids.'
    print '3. Leave.'
    a=raw_input('> ')
    self.ClearScreen()
    if a=='1':
     print 'You ask what happened.'
     print 'The knight responds,  "We were raiding the goblin village in the forest. I got wounded,  hopefully the healer will come soon. Can you help with the raid? There will be a reward of 250 self.GP for each killed goblin when you finished,  talk to the mayor when your done.".'
     print
     print 'Kill some goblins in the goblin village then talk to mayor to get a gold reward.'
    elif a=='2':
     print 'You ask about other raids.'
     print 'The knight says weakly,  "I heard about another raid on the orc kingdom but it sounds very dangerous not very many people come back from that one alive. Since it is so dangerous the mayor will give you 500 GP per killed orc if you surivive...'
     print
     print 'Kill some orcs in the orc kingdom then talk to mayor to get a gold reward.'
    elif a=='3':
     self.checkLocation(location)
    self.checkLocation(location)
   elif b=='3':
    print 'You are now in the forest.'
    print '1. Go to goblin village.'
    print '2. Go to orc kingdom.'
    print '3. Go back.'
    a=raw_input('> ')
    self.ClearScreen()
    if a=='1':
     won=False
     for i in xrange(0, self.playerLevel*2):
      enemyType=random.randrange(0, 4)
      enemyLevel=random.randrange(1, 11)*self.playerLevel # fair level algorythm
      enemyGender=random.randrange(0, 2)
      if enemyType==0:
       won=self.battleEnemy('Goblin Knight', enemyGender, 9*enemyLevel, 3.5*enemyLevel, enemyLevel, 'sword', 'melee', 0.80)
      elif enemyType==1:
       won=self.battleEnemy('Goblin Archer', enemyGender, 8*enemyLevel, 2.5*enemyLevel, enemyLevel, 'bow', 'ranged', 0.90)
      elif enemyType==2:
       won=self.battleEnemy('Goblin Mage', enemyGender, 5*enemyLevel, 3*enemyLevel, enemyLevel, 'water bolt', 'magic', 0.90)
      if won==True:
       self.goblinsKilled+=1
       XP=enemyLevel*25
       print 'Gained '+str(XP)+' XP.'
       self.playerXP+=XP
       won=False
    elif a=='2':
     won=False
     for i in xrange(0, self.playerLevel*2):
      enemyType=random.randrange(0, 4)
      enemyLevel=random.randrange(1, 11)*self.playerLevel # fair level algorythm
      enemyGender=random.randrange(0, 2)
      if enemyType==0:
       won=self.battleEnemy('Orc Knight', enemyGender, 9*enemyLevel, 5*enemyLevel, enemyLevel, 'club', 'melee', 0.70)
      elif enemyType==1:
       won=self.battleEnemy('Orc Archer', enemyGender, 8*enemyLevel, 3.5*enemyLevel, enemyLevel, 'crossbow', 'ranged', 0.80)
      elif enemyType==2:
       won=self.battleEnemy('Orc Mage', enemyGender, 7*enemyLevel, 4*enemyLevel, enemyLevel, 'water strike', 'magic', 0.80)
      if won==True:
       self.orcsKilled+=1
       XP=enemyLevel*25
       print 'Gained '+str(XP)+' XP.'
       self.playerXP+=XP
       won=False
    if self.playerXP>=self.playerNextLevelXP:
     self.playerXP=0
     self.playerLevel+=1
     self.playerNextLevelXP=self.playerLevel*300*2
     self.playerMaxHealth+=25
     self.playerHealth=self.playerMaxHealth
     print 'You leveled up!'
     print 'You are now level '+str(self.playerLevel)+'! 0/'+str(self.playerNextLevelXP)+' XP,  +25 max health.'
    elif a=='3':
     self.checkLocation(location)
   elif b=='4':
    location='town hall'
   self.checkLocation(location)
Game()
