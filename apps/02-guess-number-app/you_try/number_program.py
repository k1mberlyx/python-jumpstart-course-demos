import random

print('-------------------------------------')
print('    GUESS THAT NUMBER GAME')
print('-------------------------------------')
print(' ')

the_number = random.randint(1, 100)
guess = -1

name = input('What is your name? ')

while guess != the_number:
    guess_text = input('Enter a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry, {1} your guess of {0} was too low!'.format(guess, name) )
    elif guess > the_number:
        print('Too high!')
    else:
        print('You win!')

print('Done')