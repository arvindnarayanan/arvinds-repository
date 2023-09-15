# Sorts a list from least to greatest using the bubble sorting method

from time import sleep
from random import sample, randint

mylist = sample(range(1, 25), randint(5,13))

n = len(mylist)


def swap(x, y):
    yvalue = y
    y = x
    x = yvalue
    return x, y


print("Your list is: " + str(mylist))

for i in range(n - 1):
    for j in range(n - 1):
        if mylist[j + 1] < mylist[j]:
            (mylist[j], mylist[j + 1]) = swap(mylist[j], mylist[j + 1])

sleep(1.25)
print("Your list sorted from small to big is: " + str(mylist))
