#using random number generator to generate any random number between 0 and 100.

import random

print("======Guess The Number======")
rand_number = random.randint(0,100)
number_of_guess = 15
print("Clue: number is between 0-100")
while(number_of_guess > 0):
    print('life: ',end='')
    for i in range(number_of_guess):
        print("<3 ", end='')
    g_number = int(input("\nYour Guess: "))
    if(g_number == rand_number):
        print("!!Congratulations!!")
        print("Your guess is correct.")
        break
    elif(g_number > rand_number):
        print("Your number is greater than the actual number")
    else:
        print("Your number is lesser than the actual number")
    number_of_guess -= 1

if(number_of_guess == 0):
    print("You loose all your chances :-(")
    print("Actual number is- ",rand_number)
    print("!!Game Over!!")
else:
    print("You took ",15-number_of_guess+1,"guesses.")
