#Character creation:


protagonist_name = input('What is your name?')
print('My name is', protagonist_name)

import time
time.sleep(1)
print('Nice to meet you', protagonist_name,'!')
time.sleep(1)
#Class creation. 'Are you sure?'loop terug naar hier.
protagonist_class = input('What class are you? You can choose warrior, priest, mage or thief!)')

import random
def class_strenght(str):
    if protagonist_class == 'warrior' or protagonist_class == 'Warrior':
        str = random.randint(10, 18)
            print('Your strenght is', str)
    elif protagonist_class == 'priest' or protagonist_class == 'Priest':
        str = random.randint(8, 16)
            print('Your strenght is', str)
    elif protagonist_class == 'thief' or protagonist_class == 'Thief':
        str = random.randint(6, 14)
            print('Your strenght is', str)
    elif protagonist_class == 'mage' or protagonist_class == 'Mage':
        str = random.randint(4, 12)
            print('Your strenght is', str)
    else:
        rint('Error')