print('''
A game of Life

Rules:
1. Guess the number correctly (0-100)
2. You will get only 5 guesses

Finale:
1. If you win and get a rose (---<3)
2. If you loose then you are FUCKed up!
''')
import random

print("======Guess The Number======")

rand_number = random.randint(0,100) # using random number generator to generate any random number between 0 and 100
number_of_guess = c = 5
score = 100

while c > 0:
    print('life: ' + '<3 ' * c)
    g_number = int(input("\nYour Guess: "))
    if g_number == rand_number:
        print('''
!!Congratulations!!
Your guess is correct :-)
Take this (---<3) give it to your GF in front of your Wife!
''')
        break
    elif g_number > rand_number:
        print("Your number is greater than the actual number")
    else:
        print("Your number is lesser than the actual number")
    c -= 1

if c != 0:
    print("You took",number_of_guess - c + 1,"guesses.")
else:
    print(f'''
Actual number is: {rand_number}
FUCK you bitch!
Take this (->O)
''')
print(f'Your score: {score - 20*(number_of_guess - c)}')
