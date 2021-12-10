import random 
print("Welcome to the dice roller!")

while True:
    dice_size= input("What dice size?: ")
    try:
        dice_size = int(dice_size)
    except:
        print("invalid input!")
    if dice_size in range(1, 1000):
        break

print(random.randint(1, dice_size))