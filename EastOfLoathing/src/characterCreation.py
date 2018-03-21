#Character creation:

import random
import time

class CharacterCreation(object):
    strength  = 0;     
    intelligence  = 0; 
    constitution  = 0; 
    dexterity  = 0;
    hitpoints  = 50; 

    def charCreate(self):
        protagonist_name = input('What is your name?')
        print('My name is', protagonist_name)

        time.sleep(1)
        print('Nice to meet you', protagonist_name,'!')
        time.sleep(1)

        flag = 'no';
        while (flag == 'no'):
            protagonist_class = input('What class are you? You can choose warrior, priest, mage or thief!')
            prot =  protagonist_class.lower()   
            print(prot)
                
        while(prot !='warrior' and prot != 'priest' and prot != 'thief' and prot != 'mage'):
            print('You did not pick a class, please try again') 
            protagonist_class = input('What class are you? You can choose warrior, priest, mage or thief!') 
            prot =  protagonist_class.lower()  
         
        print('are you sure you want to be a', protagonist_class)
        flag = input('Yes or No?').lower()

    def class_strenght(self):
        if prot == 'warrior': 
            strength = random.randint(10, 18)
            print('Your strenght is', strength)
        elif prot == 'priest':
            strength = random.randint(8, 16)
            print('Your strenght is', strength)
        elif prot == 'thief': 
            strength = random.randint(6, 14)
            print('Your strenght is', strength)
        else:
                strength = random.randint(4, 12)
                print('Your strenght is', strength)
        
    def class_constitution(self):
        if prot == 'warrior': 
            constitution = random.randint(10, 18)
            print('Your constitution is', constitution)
        elif prot == 'priest':
            constitution = random.randint(10, 18)
            print('Your constitution is', constitution)
        elif prot == 'thief': 
            constitution = random.randint(8, 14)
            print('Your constitution is', constitution)
        else:
            constitution = random.randint(6, 14)
            print('Your constitution is', constitution)
        
    def class_dexterity(self):
        if prot == 'warrior': 
            dexterity = random.randint(6, 14)
            print('Your dexterity is', dexterity)
        elif prot == 'priest':
            dexterity = random.randint(6, 12)
            print('Your dexterity is', dexterity)
        elif prot == 'thief': 
            dexterity = random.randint(10, 18)
            print('Your dexterity is', dexterity)
        else:
            dexterity= random.randint(4, 12)
            print('Your dexterity is', dexterity)
        
    def class_intelligence(self):
        if prot == 'warrior': 
            intelligence = random.randint(4, 12)
            print('Your intelligence is', intelligence)
        elif prot == 'priest':
            intelligence = random.randint(6, 14)
            print('Your intelligence is', intelligence)
        elif prot == 'thief': 
            intelligence = random.randint(8, 16)
            print('Your intelligence is', intelligence)
        else:
            intelligence = random.randint(12, 18)
            print('Your intelligence is', intelligence)       

    def starting_hitpoints(self):
        self.hitpoints += (self.constitution - 10) * 5
        print('You have %s hitpoints' % hitpoints)

    def controller(self):
        self.charCreate()
        self.class_strenght()  
                   

