# MINI PROJECT
# P1>> GENERATE RANDOM PASSWORD

import random 
target = random.randint(1,150) # Gerate random number 

while True:
    userChoice = input("--Guess the number or for Quite press Q  ")

    if userChoice == "Q":
        break

    userChoice = int(userChoice)
    if userChoice == target:
       print("--Success : Correct Guess")
       break
    elif userChoice < target:
        print("You Guess too Small : Guess bigger number -- ")
    else:
        userChoice > target
        print("You Guess too big: Guess Smaller  number -- ")

print("----GAME OVER ----")


# ---RANDOM PASSWORD GENERATE---
import random
import string 
pass_len = 12
choice_pass = string.ascii_letters + string.punctuation + string.digits
password = ""
for i in range(pass_len):
    password += random.choice(choice_pass)

print("password :",password)

#another way  list comprehence __ List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list. [function for i in range(n)]

pass_word = "".join([random.choice(choice_pass) for i in range(pass_len)])
print("password:",pass_word)



