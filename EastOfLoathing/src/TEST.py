#Character creation:

import random
import time

protagonist_name = input('What is your name?')
print('My name is', protagonist_name)


time.sleep(1)
print('Nice to meet you', protagonist_name,'!')
time.sleep(1)
#Class creation. 'Are you sure?'loop terug naar hier.
protagonist_class = input('What class are you? You can choose warrior, priest, mage or thief!')

power  = 0;
  
def class_strenght(power):
    if protagonist_class == 'warrior' or protagonist_class == 'Warrior':
        power = random.randint(10, 18)
        print('Your strenght is', power)
    elif protagonist_class == 'priest' or protagonist_class == 'Priest':
        power = random.randint(8, 16)
        print('Your strenght is', power)
    elif protagonist_class == 'thief' or protagonist_class == 'Thief':
        power = random.randint(6, 14)
        print('Your strenght is', power)
    elif protagonist_class == 'mage' or protagonist_class == 'Mage':
        power = random.randint(4, 12)
        print('Your strenght is', power)
    else:
        print('Error')
        
#main functie toegevoegd. Eigenlijk moet er een main class met een main function. Dan lus van class naar classe en van function naar function.         
def main():          
        class_strenght(power)
        
main()        
        