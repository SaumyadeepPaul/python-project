import random

min_val = 1
max_value = 6
roll_dice  = str(input("Would you want to roll the dice: "))
 
if roll_dice == "yes" or roll_dice == "y":
    print(f"Rolling dice... your dice is {random.randint(min_val, max_value)}")
    
else:
    roll_dice == "no" or roll_dice == "n"
    print("Dice stopped!")
    


