from random import randint
from time import sleep

num = randint(1, 15)

for i in range(num):
    print("Turtlebunny")
    sleep(0.3)

print("'Turtlebunny' has been printed " + str(num) + " times.")
