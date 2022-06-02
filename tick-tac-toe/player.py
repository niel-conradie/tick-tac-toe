import random


class Player:
    """ A class to represent a player. """

    def __init__(self, letter):
        """ Initialize class attributes. """
        self.letter = letter

    def move(self, game):
        """ Verifying a spot for the next move. """
        pass


class HumanPlayer(Player):
    """ A class to represent a human player. """

    def __init__(self, letter):
        """ Initialize attributes of parent class. """
        super().__init__(letter)

    def move(self, game):
        """ Verifying the player choice for the next move. """
        valid_square = False
        value = None
        while not valid_square:
            square = input(
                f"\nPlayer '{self.letter.upper()}' turn. Pick a square 0 - 8: ")
            try:
                value = int(square)
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("\nInvalid square. Please try again.")
        return value


class EasyComputerPlayer(Player):
    """ A class to represent an easy computer player. """

    def __init__(self, letter):
        """ Initialize attributes of parent class. """
        super().__init__(letter)

    def move(self, game):
        """ Verifying a random spot for the next move. """
        square = random.choice(game.available_moves())
        return square
