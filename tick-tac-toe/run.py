import sys

from tic_tac_toe import TicTacToe


def run():
    """Tic-Tac-Toe."""
    run = TicTacToe()

    try:
        # Starting the game.
        run.start_game()
    except KeyboardInterrupt:
        # Stopping the game.
        sys.exit("\n\nProgram Terminated")


if __name__ == "__main__":
    run()
