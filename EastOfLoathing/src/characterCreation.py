#Character creation:

import random
import time

protagonist_name = input('What is your name?')
print('My name is', protagonist_name)


time.sleep(1)
print('Nice to meet you', protagonist_name,'!')
time.sleep(1)
#Class creation. 'Are you sure?'loop terug naar hier.

flag = 'no';
while (flag == 'no'):
    protagonist_class = input('What class are you? You can choose warrior, priest, mage or thief!')
    prot =  protagonist_class.lower()   
    print(prot)
                
    while(prot !='warrior' and prot != 'priest' and prot != 'thief' and prot != 'mage'):
        print('You did not pick a class, please try again') 
        protagonist_class = input('What class are you? You can choose warrior, priest, mage or thief!') 
        prot =  protagonist_class.lower()  
         
    flag = input('are you sure? Yes or No?').lower()

#testprint
print(protagonist_class)
print(flag)

power  = 0; 
def class_strenght(power):
    if prot == 'warrior': 
        power = random.randint(10, 18)
        print('Your strenght is', power)
    elif prot == 'priest':
        power = random.randint(8, 16)
        print('Your strenght is', power)
    elif prot == 'thief': 
        power = random.randint(6, 14)
        print('Your strenght is', power)
    elif prot == 'mage':
        power = random.randint(4, 12)
        print('Your strenght is', power)
    else:
        print('Error')
        
#main functie toegevoegd. Eigenlijk moet er een main class met een main function. Dan lus van class naar classe en van function naar function.         
def main():          
        class_strenght(power)
        
main()        
        