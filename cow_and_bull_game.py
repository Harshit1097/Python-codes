# Create a program that will play the “cows and bulls” game with the user. The game works like this: Randomly generate a 4-digit number.
# Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”.
#  For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how
#  many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of
#  guesses the user makes throughout teh game and tell the user at the end.

import random
alist = random.sample(range(10), 4)
num = [str(item) for item in alist]               # num is a list of digits of the 4 digit random number

counter = 0
while True:
    user_input = input('Enter a 4-digit number: ')
    num_user = [str(item) for item in user_input]  # num_user is a list of digits of the 4-digit number entered by user
    counter += 1
    cows = 0
    bulls = 0

    for i in range(len(num)):
        if num[i] == num_user[i]:
            cows += 1
        elif (num[i] in num_user) and (num[i] != num_user[i]):
            bulls += 1
    print(f'cows: {cows} and bulls: {bulls}')

    if cows == 4:
        break
    else:
        print('Try again\n')

print('You have made the right guess! Game over')
print(f'You took {counter} guesses to arrive at the right number')
