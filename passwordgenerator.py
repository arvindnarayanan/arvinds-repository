import random
import time

characters = ['a', 'b', 'c', 'd', 'e',
              'f', 'g', 'h', 'i', 'j',
              'k', 'l', 'm', 'n', 'o',
              'p', 'q', 'r', 's',
              't', 'u', 'v', 'w', 'x',
              'y', 'z', '1', '2', '3',
              '4', '5', '6', '7', '8',
              '9', '0', 'A', 'B', 'C',
              'F', 'G', 'H', 'I', 'J',
              'K', 'L', 'M', 'N',
              'O', 'P', 'Q', 'R', 'S',
              'T', 'U', 'V', 'W', 'X', 'Y',
              'Z', '!', '@', '#', '$', '%', '^', '&', '*']

print("Hello! welcome to the password generator!")
time.sleep(1)
print("This project will give you a random, safe password")
time.sleep(1)
print("Let's get started!")
time.sleep(1)

length = input("How long (In characters) do you want your password to be?")
length = int(length)

print("Shuffling characters...")
time.sleep(3)
print("Generating password...")
time.sleep(3)
pwd_list = random.choices(characters, k = length)
paswd = ""
for i in range(length):
    paswd = paswd + pwd_list[i]
time.sleep(1.5)
print("Your new super safe password is: " + paswd)
time.sleep(1.5)
print("Make sure to remember it!")
