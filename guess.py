# A guessing game
import random

guess_taken=0

my_name=input('hi there!, What is your name: ')
print(' ')

number=random.randint(1,25)

print('well Mr '+my_name+' I am thinking of a number between 1 and 25')
print('')

for guess_taken in range(6):
    guess=int(input('take a wild guess buddy: '))
    print(' ')
    if guess<number:
        print(' your guess is too low dude !')
        print('                             ')
    if guess>number:
        print(' your guess is too high man !')
        print('                             ')
    
    if guess==number:
        break
if guess==number:
    guess_taken=str(guess_taken+1)
    print('good job dude, '+my_name+' You nailed this in '+guess_taken+' guesses!, awesome')
    print(' ')
if guess!=number:
    number=str(number)
    print('No go man. Thenumber I was thinking of is '+number+'.')
