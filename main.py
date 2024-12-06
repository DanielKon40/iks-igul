
"""The main"""

from PyQt5 import QtWidgets
from game_code import TicTacToeGame
from GUI import Ui_MainWindow
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    game = TicTacToeGame()
    game.show()
    sys.exit(app.exec_())
