import random

num = (random.randint(0,9))
print('Number Guessing game')
print('Guess a number (between 1 and 9)')
guess_limit = 5
guess_count = 0
while guess_count<guess_limit:
    guess = int(input('Guess a number: '))
    if guess == num:
        print('Congratulations! You won! ;)')
        break
    else:
        print('Sorry, but you lost :( , the number is somewhere near ', guess)
