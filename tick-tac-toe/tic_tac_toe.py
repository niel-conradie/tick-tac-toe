from math import floor
from time import sleep

from player import HumanPlayer, EasyComputerPlayer, HardComputerPlayer


class TicTacToe:
    """A class to represent a Tick-Tac-Toe game."""

    def __init__(self):
        """Initialize class attributes."""
        self.board = self.create_board()
        self.current_winner = None

    @staticmethod
    def player_x_input():
        """Requesting user input and validating choice."""
        while True:
            try:
                user_input = int(input("Player X: "))
            except ValueError:
                print("\nThat is not a number.\n")
                continue

            choices = [1, 2, 3]
            if user_input not in choices:
                print(f"\n{user_input} is not an valid choice!\n")
                continue
            else:
                return user_input

    @staticmethod
    def player_o_input():
        """Requesting user input and validating choice."""
        while True:
            try:
                user_input = int(input("Player O: "))
            except ValueError:
                print("\nThat is not a number.\n")
                continue

            choices = [1, 2, 3]
            if user_input not in choices:
                print(f"\n{user_input} is not an valid choice!\n")
                continue
            else:
                return user_input

    @staticmethod
    def display_options(player):
        """Display user input options."""
        print(f"\nPlayer '{player.upper()}' select one option below.")
        print("\nHuman Player: Type '1'")
        print("Easy Computer: Type '2'")
        print("Hard Computer: Type '3'\n")

    @staticmethod
    def user_input_allocation(player, user_input):
        """Assign user input to appropriate type of player."""
        # Player X conditions.
        if player == "X":
            if user_input == 1:
                return HumanPlayer(player)
            if user_input == 2:
                return EasyComputerPlayer(player)
            if user_input == 3:
                return HardComputerPlayer(player)

        # Player O conditions.
        if player == "O":
            if user_input == 1:
                return HumanPlayer(player)
            if user_input == 2:
                return EasyComputerPlayer(player)
            if user_input == 3:
                return HardComputerPlayer(player)

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
        row_index = floor(square / 3)
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

    def game(self, player_x, player_o, print_game=True):
        """Start game with player_x and player_o."""
        if print_game:
            print()
            self.display_board_numbers()

        # Starting letter.1
        letter = "X"

        while self.empty_squares():
            # Selecting appropriate player.
            if letter == "O":
                square = player_o.move(self)
            else:
                square = player_x.move(self)

            # Function to make a move.
            if self.valid_move(square, letter):
                if print_game:
                    print(f"\n{letter} makes a move to square {square}\n")
                    self.display_board_numbers()
                    print("-------------")
                    self.display_board()

                if self.current_winner:
                    if print_game:
                        print(f"\nPlayer {letter} Wins!")
                    return letter

                # Switching players.
                letter = "O" if letter == "X" else "X"

            sleep(0.5)

        if print_game:
            print("\nTie!")

    def start_game(self):
        """Starting the tic-tac-toe game."""
        x = "X"
        # Display player X options.
        self.display_options(x)
        # Requesting user input.
        player_x_input = self.player_x_input()
        # Assign player X input to appropriate type of player.
        player_x = self.user_input_allocation(x, player_x_input)

        o = "O"
        # Display player O options.
        self.display_options(o)
        # Requesting user input.
        player_o_input = self.player_o_input()
        # Assign player O input to appropriate type of player.
        player_o = self.user_input_allocation(o, player_o_input)

        while True:
            # Starting game and passing player inputs as arguments.
            self.game(player_x, player_o, print_game=True)
            # Requesting user input.
            self.restart()

            continue

    @staticmethod
    def restart():
        """Requesting user input and validating choice."""
        while True:
            print("\nPlay Again?")
            print("Yes: Type '1'")
            print("No: Type '2'")

            try:
                user_input = int(input("\nEnter: "))
            except ValueError:
                print("\nThat is not a number.")
                continue

            # User input validation conditions.
            choices = [1, 2]
            if user_input not in choices:
                print(f"\n{user_input} is not an valid choice!")
                continue
            elif user_input == 1:
                return
            elif user_input == 2:
                print("\nThank you for playing!")
                quit()
