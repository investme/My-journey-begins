import random
import time

def display_intro():
    print('''You are in a land full of dragons. As you are walking, you see
two caves in front of you. In one cave, there is a friendly dragon and will
give you all his gold and treasure. But, in the other cave, a very hungry dragon
lives and will eat you alive. You have to choose the right cave.''')
    print()

def choose_cave():
    cave=''
    while cave!='1' and cave!='2':
        print('which cave will you choose ? (1 or 2)')
        cave=input()
    return cave

def check_cave(chosen_cave):
    print('you approach the cave slowly,...')
    print()
    time.sleep(3)
    print('Night is approaching and it is dark and spooky...')
    print()
    time.sleep(2)
    print('A large dragon with ugly teeth jumps out in front of you !!! The dragon opens his jaws and ...')
    print()
    time.sleep(2)

    friendly_cave=random.randint(1,2)

    if chosen_cave==str(friendly_cave):
        print('gives you his treasure and you are a fucking millionaire')
        print()
    else:
        print('Dragon is gonna eat your ass in one bite, yummmmm!!')
        print()
play_again='yes'
while play_again=='yes' or play_again=='y':
    display_intro()
    cave_number=choose_cave()
    check_cave(cave_number)

    print('Do you want to try your luck again?(yes or no)')
    play_again=input()
print('        Game Over Buddy      ')
print('        ---------------      ')




    
