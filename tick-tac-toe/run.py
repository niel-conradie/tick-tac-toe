from tic_tac_toe import TicTacToe


if __name__ == "__main__":
    run = TicTacToe()

    try:
        # Starting the game.
        run.start_game()
    except KeyboardInterrupt:
        # Stopping the game.
        quit("\n\nProgram Terminated")
