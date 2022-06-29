from tic_tac_toe import TicTacToe


def run():
    """Tic-Tac-Toe."""
    game = TicTacToe()

    x = "X"
    # Display player X options.
    game.display_options(x)
    # Requesting user input.
    player_x_input = game.player_x_input()
    # Assign player X input to appropriate type of player.
    player_x = game.user_input_allocation(x, player_x_input)

    o = "O"
    # Display player O options.
    game.display_options(o)
    # Requesting user input.
    player_o_input = game.player_o_input()
    # Assign player O input to appropriate type of player.
    player_o = game.user_input_allocation(o, player_o_input)

    while True:
        start = TicTacToe()
        # Starting game and passing player inputs as arguments.
        game.start_game(start, player_x, player_o, print_game=True)
        # Requesting user input.
        game.restart()

        continue


if __name__ == "__main__":
    run()
