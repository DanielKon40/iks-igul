
"""Creating the playing board"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 672)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.buttons = []
        self.a_1 = QtWidgets.QPushButton(self.centralwidget)
        self.a_1.setGeometry(QtCore.QRect(210, 100, 131, 111))
        self.a_1.setMouseTracking(False)
        self.a_1.setTabletTracking(False)
        self.a_1.setAutoFillBackground(False)
        self.a_1.setText("")
        self.a_1.setAutoDefault(True)
        self.a_1.setObjectName("a_1")
        self.buttons.append(self.a_1)

        self.b_1 = QtWidgets.QPushButton(self.centralwidget)
        self.b_1.setGeometry(QtCore.QRect(340, 100, 131, 111))
        self.b_1.setText("")
        self.b_1.setDefault(False)
        self.b_1.setFlat(False)
        self.b_1.setObjectName("b_1")
        self.buttons.append(self.b_1)
        self.c_1 = QtWidgets.QPushButton(self.centralwidget)
        self.c_1.setGeometry(QtCore.QRect(470, 100, 131, 111))
        self.c_1.setText("")
        self.c_1.setObjectName("c_1")
        self.buttons.append(self.c_1)
        self.a_2 = QtWidgets.QPushButton(self.centralwidget)
        self.a_2.setGeometry(QtCore.QRect(210, 210, 131, 111))
        self.a_2.setTabletTracking(False)
        self.a_2.setText("")
        self.a_2.setObjectName("a_2")
        self.buttons.append(self.a_2)
        self.b_2 = QtWidgets.QPushButton(self.centralwidget)
        self.b_2.setGeometry(QtCore.QRect(340, 210, 131, 111))
        self.b_2.setText("")
        self.b_2.setObjectName("b_2")
        self.buttons.append(self.b_2)
        self.c_2 = QtWidgets.QPushButton(self.centralwidget)
        self.c_2.setGeometry(QtCore.QRect(470, 210, 131, 111))
        self.c_2.setText("")
        self.c_2.setObjectName("c_2")
        self.buttons.append(self.c_2)
        self.a_3 = QtWidgets.QPushButton(self.centralwidget)
        self.a_3.setGeometry(QtCore.QRect(210, 320, 131, 111))
        self.a_3.setText("")
        self.a_3.setObjectName("a_3")
        self.buttons.append(self.a_3)
        self.b_3 = QtWidgets.QPushButton(self.centralwidget)
        self.b_3.setGeometry(QtCore.QRect(340, 320, 131, 111))
        self.b_3.setText("")
        self.b_3.setObjectName("b_3")
        self.buttons.append(self.b_3)
        self.c_3 = QtWidgets.QPushButton(self.centralwidget)
        self.c_3.setGeometry(QtCore.QRect(470, 320, 131, 111))
        self.c_3.setText("")
        self.c_3.setObjectName("c_3")
        self.buttons.append(self.c_3)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("Player goes first!")
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
