#Character creation:

import random
import time

class CharacterCreation(object):
    strength  = 0;     
    intelligence  = 0; 
    constitution  = 0; 
    dexterity  = 0;
    hitpoints  = 50; 
    prot = ''

    def charCreate(self):
        protagonist_name = input('What is your name?')
        print('My name is %s' % protagonist_name)

        time.sleep(1)
        print('Nice to meet you %s!' % protagonist_name)
        time.sleep(1)
  
        flag = 'no';
        while (flag == 'no'):        
            protagonist_class = input('What class are you? You can choose warrior, priest, mage or thief!')
            self.prot =  protagonist_class.lower() 
            while(self.prot !='warrior' and self.prot != 'priest' and self.prot != 'thief' and self.prot != 'mage'):
                print('You did not pick a class, please try again') 
                protagonist_class = input('What class are you? You can choose warrior, priest, mage or thief!') 
                self.prot =  protagonist_class.lower()  
        
                time.sleep(1)
      
            if protagonist_class == 'warrior':
                print(
                    '''
                Warriors are fearsome melee fighters who generally have great strenght and constitution,
                but are slower in body and mind than other classes.
                '''
                )
                time.sleep(1)
            elif protagonist_class == 'priest':
                print(
                ''''
                Unlike the pampered papal clergyman we come to expect in modern times,
                the singular devotion of priest makes them excellent combat-healers and
                with their heavy blunt religious paraphernalia they tend to be
                quite adept in headbashing their enemies into oblivion.
                '''
                )
            elif protagonist_class == 'thief':
                print(
                '''
                Congratulations! From all the classes you could choose...
                thieves are backstabbing, sneaky, unreliable scum who,
                although they would avoid a fight whenever possible and rather poison you or kill you from afar,
                rely on their dexterity to keep themself save in hand to hand combat
                '''
                )
            else:
                print(
                '''
                Due to the unreliable nature of most magic, 
                surviving mages are without exception able to use protective magic to 
                prevent self-combustion in case a spell goes wrong. Highly intelligent out of necessity, 
                mages wield magic in a ruthless yet unpredictable way. 
                '''
                )
            time.sleep(1)
            flag = input('Are you sure you want to be a %s? Yes or No' % protagonist_class).lower()
            
        print('Good choice! I\'ve always wanted to be a %s.' % protagonist_class)

    def class_strenght(self):
        
        prot = self.prot
        time.sleep(1)
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
        self.strenght = strength
        
    def class_constitution(self):
        
        prot = self.prot
        time.sleep(1)
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
        self.constitution = constitution
        
    def class_dexterity(self):
        
        prot = self.prot
        time.sleep(1)
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
        self.dexterity = dexterity
        
    def class_intelligence(self):
        
        prot = self.prot
        time.sleep(1)
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
        self.intelligence = intelligence     

    def starting_hitpoints(self):
        
        constitution = self.constitution
        if constitution >= 16:
            self.hitpoints += (constitution - 10) * 6
        elif constitution >= 13:
            self.hitpoints += (constitution - 10) * 5
        elif constitution >= 10:
            self.hitpoints += (constitution - 10) * 4
        else:
            self.hitpoints += (constitution - 10) * 2
        time.sleep(1)
        print('You have %s hitpoints' % self.hitpoints)
    
    #def stats(self, a, b, c, d, e,):
    #   stats = [4]
        #stats = ['strenght' : a, b,c,d,e];
        #print(stats)
    def controller(self):
        self.charCreate()
        self.class_strenght()
        self.class_constitution()  
        self.class_dexterity()
        self.class_intelligence()
        self.starting_hitpoints()
        #self.stats(self.strenght, self.constitution, self.dexterity, self.intelligence, self.hitpoints)    
            
