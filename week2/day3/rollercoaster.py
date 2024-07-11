print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    else:
        print("Adult tickets are $12.")
        bill = 12
    wants_photo = input("Would you like a photo taken? (Y/N) ")
    if wants_photo == "Y" or wants_photo == "y":
        bill += 3
    print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you are not tall enough to ride.")