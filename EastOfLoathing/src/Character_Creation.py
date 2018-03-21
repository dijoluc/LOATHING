#Character creation:

import random
import time

protagonist_name = input('What is your name?')
print('My name is %s' % (protagonist_name))


time.sleep(1)
print('Nice to meet you %s!' % (protagonist_name))
time.sleep(1)
#Class creation. 'Are you sure?'loop terug naar hier.
print('Dont worry about choosing a race, there is only the *************** motherfuckers!')

time.sleep(1)


while True:
    protagonist_class = input('What class are you? You can choose warrior, priest, mage or thief!')
    if protagonist_class == 'warrior' or classchoice == 'priest' or classchoice == 'thief' or classchoice == 'mage':
        time.sleep(1)
        print('Good choice!')
        break
    else:
        print('WRONG! PLease Try again!')
        input('What class are you? You can choose warrior, priest, mage or thief!')

protagonist_class = '';

classchoice = input('What class are you? You can choose warrior, priest, mage or thief!')
classchoice = classchoice.lower()
while classchoice != 'warrior' or classchoice != 'priest' or classchoice != 'thief' or classchoice != 'mage':
    time.sleep(1)
    print('WRONG! PLease Try again!')
    input('What class are you? You can choose warrior, priest, mage or thief!')
    protagonist_class.append(classchoice)
else:
    time.sleep(1)
    print('Good choice!')
    protagonist_class.append(classchoice)
    
strength  = 0;
  
def class_strength(strength):
    if classchoice == 'warrior':
        strength = random.randint(10, 18)
        print('Your strength is %s' % (strength))
    elif classchoice == 'priest':
        strength = random.randint(8, 16)
        print('Your strength is  %s' % (strength))
    elif classchoice == 'thief':
        strength = random.randint(6, 14)
        print('Your strength is %s' % (strength))
    elif classchoice == 'mage':
        strength = random.randint(4, 12)
        print('Your strength is %s' % (strength))
    else:
        print('Try again')
        print(classchoice)
        
constitution  = 0;
  
def class_constitution(constitution):
    if protagonist_class == 'warrior':
        constitution = random.randint(10, 18)
        print('Your constitution is %s' % (constitution))
    elif protagonist_class == 'priest':
        constitution = random.randint(8, 16)
        print('Your constitution is  %s' % (constitution))
    elif protagonist_class == 'thief':
        constitution = random.randint(6, 14)
        print('Your constitution is %s' % (constitution))
    elif protagonist_class == 'mage':
        constitution = random.randint(4, 12)
        print('Your constitution is %s' % (constitution))
    else:
        print('Try again')
        print(protagonist_class)
        
#main functie toegevoegd. Eigenlijk moet er een main class met een main function. Dan lus van class naar classe en van function naar function.         
def main():           
        class_strength(strength)
        class_constitution(constitution)

main()        
        