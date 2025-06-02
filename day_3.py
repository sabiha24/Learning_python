print("knowing the given number is odd or even!")
n=int(input("type down the input number: "))
if n%2==0:
    print("the given number is EVEN")
else:
    print("the given number is ODD")
--------------------------------------------------------------
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bil=5
        print("Please pay $5.")
    elif age <= 18:
        bill=7
        print("Please pay $7.")
    else:
        bill=12
        print("Please pay $12.")
    pic=input("Do u want a photo take. Type y for Yes n for No.")
    if pic=="y":
        bill+=3
        print(f"ur final bill is ${bill}")
    else:
        print(f"ur final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
