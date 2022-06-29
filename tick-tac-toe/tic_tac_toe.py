import math

from time import sleep


class TicTacToe:
    """A class to represent a Tick-Tac-Toe game."""

    def __init__(self):
        """Initialize class attributes."""
        self.board = self.create_board()
        self.current_winner = None

    @staticmethod
    def create_board():
        """Creating the board."""
        return [" " for _ in range(9)]

    def display_board(self):
        """Adding rows to the board."""
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def display_board_numbers():
        """Adding numbers that correspond to each box."""
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def empty_squares(self):
        """Verifying empty board squares."""
        return " " in self.board

    def number_empty_squares(self):
        """Verifying the number of empty squares."""
        return self.board.count(" ")

    def available_moves(self):
        """Verifying available moves."""
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def valid_move(self, square, letter):
        """Verifying a valid move."""
        if self.board[square] == " ":
            self.board[square] = letter
            if self.win_condition(square, letter):
                self.current_winner = letter
            return True
        return False

    def win_condition(self, square, letter):
        """Verifying the winner."""
        row_index = math.floor(square / 3)
        row = self.board[row_index * 3 : (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        column_index = square % 3
        column = [self.board[column_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal_1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal_1]):
                return True

            diagonal_2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal_2]):
                return True
        return False

    @staticmethod
    def start_game(game, player_x, player_o, print_game=True):
        """Start game with player_x and player_o."""

        if print_game:
            print()
            game.display_board_numbers()

        # Starting letter.
        letter = "X"

        while game.empty_squares():
            # Selecting appropriate player.
            if letter == "O":
                square = player_o.move(game)
            else:
                square = player_x.move(game)

            # Function to make a move.
            if game.valid_move(square, letter):
                if print_game:
                    print(f"\n{letter} makes a move to square {square}\n")
                    game.display_board_numbers()
                    print("-------------")
                    game.display_board()

                if game.current_winner:
                    if print_game:
                        print(f"\nPlayer {letter} Wins!")
                    return letter

                # Switching players.
                letter = "O" if letter == "X" else "X"

            sleep(0.5)

        if print_game:
            print("\nTie!")

    @staticmethod
    def restart():
        """Requesting user input and validating choice."""
        while True:
            user_input = input("\nRestart? Yes/No: ").lower()
            choices = ["yes", "no"]
            if user_input not in choices:
                print("\nPlease type 'yes' or 'no'")
                continue

            # User input conditions.
            if user_input == "yes":
                return
            if user_input == "no":
                print("\nThank you for playing!")
                quit()
