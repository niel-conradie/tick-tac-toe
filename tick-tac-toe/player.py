import random
import math


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


class HardComputerPlayer(Player):
    """ A class to represent a hard computer player. """

    def __init__(self, letter):
        """ Initialize attributes of parent class. """
        super().__init__(letter)

    def move(self, game):
        """ Verifying best spot for the next move. """
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.min_max(game, self.letter)['position']
        return square

    def min_max(self, state, player):
        """ Minimize moves and maximize score algorithm. """
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # Verifying previous move.
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.number_empty_squares() + 1)
                    if other_player == max_player else -1 * (state.number_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        # Initialize dictionaries.
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        # Verifying a possible move.
        for possible_move in state.available_moves():
            state.valid_move(possible_move, player)
            simulated_score = self.min_max(state, other_player)

            # Undo move.
            state.board[possible_move] = ' '
            state.current_winner = None
            simulated_score['position'] = possible_move

            # Updating dictionaries if necessary.
            if player == max_player:
                if simulated_score['score'] > best['score']:
                    best = simulated_score
            else:
                if simulated_score['score'] < best['score']:
                    best = simulated_score
        return best
