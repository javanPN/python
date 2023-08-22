import random
def play():
    isExit = False
    while isExit == False:
        user = input("Whats your Choice?'r' for rock, 'p' for paper, 's' for scissors\n")
        computer = random.choice(['r', 'p', 's'])
        if user == computer:
            print('Its a tie')
        elif is_win(user, computer):
            print('You won!')
            isExit = True
        else:
            print('You lost!')



def is_win(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())