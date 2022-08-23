print("Welcome to the quiz game!")

play = input("Would you want to play? ")

if play.lower() == "yes":
    print("Let's play...")
    

else:
    quit()

score = 0    

answer = int(input("How many continent are there in the world: "))   
if answer == 7:
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")
    

answer = int(input("How many oceans are there in the world: "))   
if answer == 5:
   print("Correct answer!")
   score += 1
else:
    print("Incorrect answer!")


answer = int(input("How many wonders are there in the world: "))   
if answer == 7:
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")


answer = int(input("How many countries are there in the world: "))   
if answer == 195:
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")


answer = input("What is the full form of GDP: ")
if answer.lower() == "gross domestic product":
   print("Correct answer!")
   score += 1 
else:
    print("Incorrect answer!")


print(f"You got {(score / 5) * 100} percent.")
