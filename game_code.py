
"""Setting the general game"""

from PyQt5 import QtCore, QtGui, QtWidgets
from GUI import Ui_MainWindow
from cpu import TicTacToeCPU
from file_export import file_export
import sys


class TicTacToeGame(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.current_turn = "X"
        self.cpu_gameplay = TicTacToeCPU(self)
        self.file_export = file_export()
        self.setup_connections()

    """Setting the buttons"""
    def setup_connections(self):
        for button in self.ui.buttons:
            button.clicked.connect(lambda checked, btn=button: self.handle_button_click(btn))

    def handle_button_click(self, button):

        if button.text() == "" and self.current_turn == "X":
            button.setText("X")
            if self.check_winner("X"):
                self.ui.label.setText("Player Wins!")
                self.end_game()
            elif self.check_tie():
                self.ui.label.setText("Tie!")
                self.end_game()
            else:
                self.ui.label.setText("CPU's Turn")
                self.current_turn = "O"
                QtCore.QTimer.singleShot(250, self.cpu_gameplay.make_move)

    def check_winner(self, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6],
        ]
        for combo in winning_combinations:
            if all(self.ui.buttons[i].text() == player for i in combo):
                return True
        return False

    def check_tie(self):
        return all(button.text() != "" for button in self.ui.buttons)

    def end_game(self):
        """Ends the game and logs the results"""
        winner = ""
        if self.ui.label.text() == "Player Wins!":
            winner = "Player"
        elif self.ui.label.text() == "CPU Wins!":
            winner = "CPU"
        elif self.ui.label.text() == "Tie!":
            winner = "Tie"

        self.file_export.log_result(winner)

        for button in self.ui.buttons:
            button.setEnabled(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    game = TicTacToeGame()
    game.show()
    sys.exit(app.exec_())


