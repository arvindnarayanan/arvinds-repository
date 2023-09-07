import time

year = int(input("Enter a year: "))
time.sleep(1)
print("Calculating...")
time.sleep(2)

if year == round(year):
    if year < 0 or year == 0:
        print("Your year should be a positive number")
    elif year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(str(year) + " is a leap year!")
            else:
                print(str(year) + " is not a leap year!")
        else:
            print(str(year) + " is a leap year!")
    else:
        print(str(year) + " is not a leap year!")
else:
    print("Your year should be a number.")

time.sleep(1)
