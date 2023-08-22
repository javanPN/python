# import random
# from words import words
# #from hangman_visual import lives_visual_dict
# import string
#
# lives_visual_dict = {
#         0: """
#                 ___________
#                | /        |
#                |/        ( )
#                |          |
#                |         / \\
#                |
#            """,
#         1: """
#                 ___________
#                | /        |
#                |/        ( )
#                |          |
#                |         /
#                |
#             """,
#         2: """
#                 ___________
#                | /        |
#                |/        ( )
#                |          |
#                |
#                |
#             """,
#         3: """
#                 ___________
#                | /        |
#                |/        ( )
#                |
#                |
#                |
#             """,
#         4: """
#                 ___________
#                | /        |
#                |/
#                |
#                |
#                |
#             """,
#         5: """
#                 ___________
#                | /
#                |/
#                |
#                |
#                |
#             """,
#         6: """
#                |
#                |
#                |
#                |
#                |
#             """,
#         7: "",
#     }
#
# def get_valid_word(words):
#     word = random.choice(words)  # randomly chooses something from the list
#     while '-' in word or ' ' in word:
#         word = random.choice(words)
#
#     return word.upper()
#
#
# def hangman():
#     word = get_valid_word(words)
#     word_letters = set(word)  # letters in the word
#     alphabet = set(string.ascii_uppercase)
#     used_letters = set()  # what the user has guessed
#
#     lives = 7
#
#     # getting user input
#     while len(word_letters) > 0 and lives > 0:
#         # letters used
#         # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
#         print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
#
#         # what current word is (ie W - R D)
#         word_list = [letter if letter in used_letters else '-' for letter in word]
#         print(lives_visual_dict[lives])
#         print('Current word: ', ' '.join(word_list))
#
#         user_letter = input('Guess a letter: ').upper()
#         if user_letter in alphabet - used_letters:
#             used_letters.add(user_letter)
#             if user_letter in word_letters:
#                 word_letters.remove(user_letter)
#                 print('')
#
#             else:
#                 lives = lives - 1  # takes away a life if wrong
#                 print('\nYour letter,', user_letter, 'is not in the word.')
#
#         elif user_letter in used_letters:
#             print('\nYou have already used that letter. Guess another letter.')
#
#         else:
#             print('\nThat is not a valid letter.')
#
#     # gets here when len(word_letters) == 0 OR when lives == 0
#     if lives == 0:
#         print(lives_visual_dict[lives])
#         print('You died, sorry. The word was', word)
#     else:
#         print('Wow! You are not that much of a monkey as I thought you were  :)', word, '!!')
#
#
# if __name__ == '__main__':
#     hangman()
#
import random

import row as row
import self as self


class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()

        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.rrandit(0, self.dim_size ** 2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size
            if board[row][col] == '*':
                continue
            board[row][col] = '*'
            bombs_planted += 1

        self.dug = set()

    def make_new_board(self):

        def assign_values_to_board(self):
            for r in range(self.dim_size):
                for c in range(self.dim_size):
                    if self.board[r][c] == '*':
                        continue
                    self.board[r][c] = self.ger_num_neighboring_boms(r, c)

    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        return num_neighboring_bombs

    def dig(self, row, col):
        self.dug.add((row, col))

#     if self.board[row][col] == '*':
#     return
#
#
# def play(dim_size=10, num_bombs=10):
#     board = Board(dim_size, num_bombs)
#
#     pass
