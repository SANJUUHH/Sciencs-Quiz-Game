print()
print()

print("********************WELCOME TO THE GENERAL SCIENCE QUIZ GAME***********************")
print()

name = input("Enter your name: ")
print("Hello " + name + ", Let's play the game!")
print()

score = 0

answer = input("What planet is known as the 'Giant Red Spot'? ")
if answer.lower() == "jupiter"  :
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")
    print()

answer = input("What is the chemical symbol for gold? ")
if answer.lower() ==  "au"  :
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")
    print()

answer = input("What is the process by which a liquid changes into a gas? ")
if answer.lower() == "evaporation" :
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")
    print() 

answer = input("What is the largest organ in the human body? ")
if answer.lower() == "skin" :
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")
    print()

answer = input("Which planet is known for its prominent ring system? ")
if answer.lower() == "saturn":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")
    print()

answer = input("What do you call the study of weather? ")
if answer.lower() == "meteorology"  :
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")
    print()

answer = input("What planet is known as the Red Planet? ")
if answer.lower() == "mars":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")
    print()

answer = input("What is the process by which plants make their own food using sunlight? ")
if answer.lower() == "photosynthesis" :
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")
    print()

answer = input("What is the hardest natural substance on Earth? ")
if answer.lower() == "diamond" :
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")
    print()

answer = input("What part of the cell contains genetic material? ")
if answer.lower() ==  "nucleus"  :
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")
    print()

def not_answered():
    if answer == None:
        print("You have not answered the question. ")
        exit()

print("You got " + str(score)+" questions correct out of 10.")
print("You got "+str((score/10)*100)+"%.")


