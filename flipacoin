from random import randint
from time import sleep

def flip_coin():
    result = randint(1,2)
    if result == 1:
        print("You got heads!")
    else:
        print("You got tails!")
    sleep(1)
    
    a = input("Would you like to flip again? ")
     
    if a.casefold() in ["y" , "yes" , "yeah"]:
        flip_coin()

    elif a.casefold() in ["n" , "no" , "nope"]:
        print("Ok bye, hope you come again!")
        sleep(2)
        quit()

    else:
        print("Your answer wasn't recognized, so we'll just assume that you don't want to flip again. So goodbye I guess, come again!")
        sleep(2)
        quit()

print("This program will flip a coin.")
sleep(1)
print("flipping.......")
sleep(2)
flip_coin()
