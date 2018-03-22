import characterCreation
import time

def main():
    characterCreation.CharacterCreation().controller()
  
if __name__ == "__main__":
    flag = 'no';
    while (flag == 'no'):
        main()
        time.sleep(1)
        print('Confirm Character Creation? This action is irreversible.')
        time.sleep(1)
        flag = input('Yes or No').lower()
        time.sleep(1)
        print('Okay lets try again!')
        time.sleep(1)
        print('--------------------------------------------------------------------------------')
        time.sleep(1)
    