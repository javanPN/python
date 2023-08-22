# def power_of_two(x):
#     y = x ** 2
#     print (f'{x} raised to the power of 2 is: {y}')
#     return y
#
# java = "is a kusu"
# print (java)
# print ("Hello world")
# # x = 2
# # print (x)
# # x = 2**2
# # print (x)
# # x = 3**2
# # print (x)
# print (power_of_two(2))
# print (power_of_two(4))
# print (2**3)
# #power_of_two("x")
#
# x = 2
# y = x
# print (f'{x}')
# print (f'{y}')
# x = 5
# print (f'{x}')
# print (f'{y}')
#
# if x > 10:
#     print("x > 10")
# else:
#     print("x <= 10")
#
# x = 0
# for i in range(1, 11):
#     print(x, i)
#     x = x + i
#     # print(x)
# print(x)
#
# num_list = [1, 3, 5, 10]
# sec_list = [1, 3, 5, 7, 9, 11]
# for i in num_list:
#     print(i)
# print(len(num_list))
# print(len(sec_list))
# third_list = [1, 2, 5, 6 ,7, 4, 3, 10, 18, 21,25, 25]
# print(len(third_list))
# for i in third_list:
#     print(i)
# #print(third_list[0])
# #print(third_list[1])
# #print(third_list)
# print(third_list[-1])
# sum = 0
# for i in third_list:
#     sum = sum + i
#     print(sum)
# print(len(third_list))
# avg = sum / len(third_list)
# print(avg)
# import statistics
# print("median:", statistics.median(third_list))
# print("mean", statistics.mean(third_list))
# print("mode", statistics.mode(third_list))
# print("level airlines stinks like butt")
# print("we should fly first class more :) ")
# print(5*"poo")
# #text = input("you smell like a fart... ")
# #print(text)
# # i = input("enter value for i: ")
# # j = input("enter value for j: ")
# # if i > j:
# #     print("i > j")
# # elif i < j:
# #     print("i < j")
# # else:
# #     print("i == j")
# pset_time = 22
# sleep_time = 22
# print(sleep_time > pset_time)
# i = 0
# while i < 3:
#     i += 1
#     print(i)
# print(i)
#print(len(s))
#print(len("abcde"))
#print(s[0])
#print(s[-3])
# for index in range(len(s)):
#     print(s[index])
#s1 = "mit u rock"
#s2 = "i rule mit"
#for is1 in range(len(s1)):
 #   for is2 in range(len(s2)):
 #       if s1[is1] == s2[is2]:
  #          print("found match",s1[is1])
#cube = 8
#print (range(cube))

#test_list = [3, 6, 7, 8, 9, 2, 1, 5]
#print("The original list : " + str(test_list))
#odd_i = []
#even_i = []
#test_var = 5
#for i in range(0, len(test_list)):
  #  if (i != test_var):
        # even_i.append(test_list[i])
  #      print(test_list[i])
    # else:
    #     odd_i.append(test_list[i])
    # print(i)

#res = odd_i + even_i


#pZPp-PP_rint("Separated odd and even index list: " + str(res))

#for i in range(1, 10, 2):
 #   print(i)
#adj = input("Adjective: ")
#verb1 = input("verb: ")
##famous_person = input("Famous person: ")

#madlib = f"Computer programming is so {adj}! it make me so poopy all the time because I love to {verb1}. \
 #   Stay hydrated and {verb2} like you are {famous_person} "
#print(madlib)



#import random
#def guess(x):
   # random_numer = random.randint(1, x)
   # guess = 0
   # while guess != random_numer:
   #     guess = int(input(f'Guess a number between 1 and {x}: '))
   #     if guess < random_numer:
   #         print('Sorry, guess again. Too low.')
    #    elif guess > random_numer:
    #        print('Sorry, guess again. Too high.')
  #  print('Wow, you dont suck that much.')


#guess(10)

#adj1 = input("Adjective1: ")
#adj2 = input("Adjective2: ")
#adj3 = input("Adjective3: ")
#adj4 = input("Adjective4: ")
#adj5 = input("Adjective5: ")
#adj6 = input("Adjective6: ")
#adj7 = input("Adjective7: ")
#verb1 = input("verb1: ")
#verb2 = input("verb2: ")
#verb3 = input("verb3: ")
#noun1 = input("noun1: ")
#pluralnoun1 = input("Plural noun1: ")
#pluralnoun2 = input("Plural noun2: ")
#pluralnoun3 = input("Plural noun3: ")
#verbed1= input("Verb-ed1: ")
#verbed2= input("Verb-ed:2 ")
#verbs1 = input("verb-s1: ")
#verbs2 = input("verb-s2: ")
#Nounfood1 = input("Noun-food1: ")
#Nounfood2 = input("Noun-food2: ")

#madlib = f"You birthday is a very {adj1} day! Birthdays are a way to {verb1} the day someone is born and to make them feel {adj2}. \
         #   Often {pluralnoun1} and {pluralnoun2} {verb2} someone a {adj3} gift for their birthday, {verbed1} in {adj4} paper, \
         #   or a {adj5} card whit a {adj6} birthday wish {verbed2} inside. You can have a {noun1} to {verb3} \
         #   your birthday where you get lots of {pluralnoun3} and everyone {verbs1} a {adj7} birthday song. The everyone {verbs2} birthday {Nounfood1} and {Nounfood2}. "
#print(madlib)



#import math
#import time
#from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


#class TicTacToe():
   # def __init__(self):
    #    self.board = self.make_board()
      #  self.current_winner = None

  #  @staticmethod
  #  def make_board():
    #    return [' ' for _ in range(9)]

   # def print_board(self):
    #    for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            #print('| ' + ' | '.join(row) + ' |')

    #@staticmethod
    #def print_board_nums():
        # 0 | 1 | 2
        #number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
       # for row in number_board:
           # print('| ' + ' | '.join(row) + ' |')

    #def make_move(self, square, letter):
      #  if self.board[square] == ' ':
       #     self.board[square] = letter
       #     if self.winner(square, letter):
       #         self.current_winner = letter
        #    return True
       # return False

    #def winner(self, square, letter):
        # check the row
       # row_ind = math.floor(square / 3)
       # row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        #if all([s == letter for s in row]):
           # return True
       # col_ind = square % 3
       # column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
       # if all([s == letter for s in column]):
        #    return True
       # if square % 2 == 0:
      #      diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
          #  if all([s == letter for s in diagonal1]):
            #    return True
          #  diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
          #  if all([s == letter for s in diagonal2]):
           #     return True
        #return False

    #def empty_squares(self):
       # return ' ' in self.board

   # def num_empty_squares(self):
       # return self.board.count(' ')

  #  def available_moves(self):
       # return [i for i, x in enumerate(self.board) if x == " "]


#def play(game, x_player, o_player, print_game=True):

    #if print_game:
     #   game.print_board_nums()

    #letter = 'X'
    #while game.empty_squares():
   #     if letter == 'O':
      #      square = o_player.get_move(game)
       # else:
     #       square = x_player.get_move(game)
     #   if game.make_move(square, letter):

       #     if print_game:
         #       print(letter + ' makes a move to square {}'.format(square))
         #       game.print_board()
           #     print('')

            #if game.current_winner:
            #    if print_game:
              #      print(letter + ' wins!')
              #  return letter  # ends the loop and exits the game
           # letter = 'O' if letter == 'X' else 'X'  # switches player

       # time.sleep(.8)

   # if print_game:
    #    print('It\'s a tie!')



#if __name__ == '__main__':
  #  x_player = SmartComputerPlayer('X')
   # o_player = HumanPlayer('O')
  #  t = TicTacToe()
   # play(t, x_player, o_player, print_game=True)


import random
import re


# lets create a board object to represent the minesweeper game
# this is so that we can just say "create a new board object", or
# "dig here", or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        # let's keep track of these parameters. they'll be helpful later
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create the board
        # helper function!
        self.board = self.make_new_board()  # plant the bombs
        self.assign_values_to_board()

        # initialize a set to keep track of which locations we've uncovered
        # we'll save (row,col) tuples into this set
        self.dug = set()  # if we dig at 0, 0, then self.dug = {(0,0)}

    def make_new_board(self):
        # construct a new board based on the dim size and num bombs
        # we should construct the list of lists here (or whatever representation you prefer,
        # but since we have a 2-D board, list of lists is most natural)

        # generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # this creates an array like this:
        # [[None, None, ..., None],
        #  [None, None, ..., None],
        #  [...                  ],
        #  [None, None, ..., None]]
        # we can see how this represents a board!

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size ** 2 - 1)  # return a random integer N such that a <= N <= b
            row = loc // self.dim_size  # we want the number of times dim_size goes into loc to tell us what row to look at
            col = loc % self.dim_size  # we want the remainder to tell us what index in that row to look at

            if board[row][col] == '*':
                # this means we've actually planted a bomb there already so keep going
                continue

            board[row][col] = '*'  # plant the bomb
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        # now that we have the bombs planted, let's assign a number 0-8 for all the empty spaces, which
        # represents how many neighboring bombs there are. we can precompute these and it'll save us some
        # effort checking what's around the board later on :)
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    # if this is already a bomb, we don't want to calculate anything
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        # let's iterate through each of the neighboring positions and sum number of bombs
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)

        # make sure to not go out of bounds!

        num_neighboring_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if r == row and c == col:
                    # our original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    def dig(self, row, col):
        # dig at that location!
        # return True if successful dig, False if bomb dug

        # a few scenarios:
        # hit a bomb -> game over
        # dig at location with neighboring bombs -> finish dig
        # dig at location with no neighboring bombs -> recursively dig neighbors!

        self.dug.add((row, col))  # keep track that we dug here

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        # self.board[row][col] == 0
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if (r, c) in self.dug:
                    continue  # don't dig where you've already dug
                self.dig(r, c)

        # if our initial dig didn't hit a bomb, we *shouldn't* hit a bomb here
        return True

    def __str__(self):
        # this is a magic function where if you call print on this object,
        # it'll print out what this function returns!
        # return a string that shows the board to the player

        # first let's create a new array that represents what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key=len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-' * str_len + '\n' + string_rep + '-' * str_len

        return string_rep


# play the game
def play(dim_size=10, num_bombs=10):
    # Step 1: create the board and plant the bombs
    board = Board(dim_size, num_bombs)

    # Step 2: show the user the board and ask for where they want to dig
    # Step 3a: if location is a bomb, show game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is at least
    #          next to a bomb
    # Step 4: repeat steps 2 and 3a/b until there are no more places to dig -> VICTORY!
    safe = True

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        # 0,0 or 0, 0 or 0,    0
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))  # '0, 3'
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue

        # if it's valid, we dig
        safe = board.dig(row, col)
        if not safe:
            # dug a bomb ahhhhhhh
            break  # (game over rip)

    # 2 ways to end loop, lets check which one
    if safe:
        print("CONGRATULATIONS!!!! YOU ARE VICTORIOUS!")
    else:
        print("SORRY GAME OVER :(")
        # let's reveal the whole board!
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)


if __name__ == '__main__':  # good practice :)
    play()