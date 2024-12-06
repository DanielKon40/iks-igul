
"""Setting the cpu's movement"""

import random


class TicTacToeCPU:
    def __init__(self, game):
        self.game = game

    def make_move(self):
        empty_buttons = [button for button in self.game.ui.buttons if button.text() == ""]
        if empty_buttons:
            chosen_button = random.choice(empty_buttons)
            chosen_button.setText("O")

            # Checks if CPU wins
            if self.game.check_winner("O"):
                self.game.ui.label.setText("CPU Wins!")
                self.game.end_game()
                return

            # Checks if the game is a tie
            if self.game.check_tie():
                self.game.ui.label.setText("It's a Tie!")
                self.game.end_game()
                return

            # Switches the turns
            self.game.ui.label.setText("Player's Turn")
            self.game.current_turn = "X"


