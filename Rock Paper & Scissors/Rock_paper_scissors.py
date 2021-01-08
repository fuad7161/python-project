import random
playGame = True
def play():
    computer_choice = random.choice(['r','p','s'])

    my_choice = input()
    if my_choice == 'Stop':
        return;
    #s > p , r > s , p > r
    if my_choice == computer_choice:
        return  'It\'s a tie'
    if(win(my_choice,computer_choice)):
        return 'You won!'
    return 'You lose! '

def win(me,com):
    return  me == 's' and com == 'p' or me == 'r' and com == 's' or \
    me == 'p' and com == 'r'

print("'r' for rock,\n's' for scissors,\n'p' for paper. \n 'Stop' for end the game")

while(playGame):
    s = play()
    if(s == None):
        playGame = False
    else :
        print(s)
