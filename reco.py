# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reco.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1881, 875)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.STOP = QtWidgets.QPushButton(self.centralwidget)
        self.STOP.setGeometry(QtCore.QRect(500, 720, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.STOP.setFont(font)
        self.STOP.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border-radius:10px;")
        self.STOP.setObjectName("STOP")
        self.EXIT = QtWidgets.QPushButton(self.centralwidget)
        self.EXIT.setGeometry(QtCore.QRect(1220, 720, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.EXIT.setFont(font)
        self.EXIT.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border-radius:10px;")
        self.EXIT.setObjectName("EXIT")
        self.imglabel = QtWidgets.QLabel(self.centralwidget)
        self.imglabel.setGeometry(QtCore.QRect(410, 120, 1111, 421))
        self.imglabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imglabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imglabel.setLineWidth(5)
        self.imglabel.setText("")
        self.imglabel.setObjectName("imglabel")
        self.TEXT = QtWidgets.QLabel(self.centralwidget)
        self.TEXT.setGeometry(QtCore.QRect(660, 50, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.TEXT.setFont(font)
        self.TEXT.setFrameShape(QtWidgets.QFrame.Box)
        self.TEXT.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TEXT.setLineWidth(2)
        self.TEXT.setText("")
        self.TEXT.setObjectName("TEXT")
        self.START = QtWidgets.QPushButton(self.centralwidget)
        self.START.setGeometry(QtCore.QRect(1100, 570, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.START.setFont(font)
        self.START.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border-radius:10px;")
        self.START.setObjectName("START")
        self.IP = QtWidgets.QLineEdit(self.centralwidget)
        self.IP.setGeometry(QtCore.QRect(700, 570, 391, 41))
        self.IP.setText("")
        self.IP.setObjectName("IP")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1881, 26))
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
        self.STOP.setText(_translate("MainWindow", "STOP"))
        self.EXIT.setText(_translate("MainWindow", "Exit"))
        self.START.setText(_translate("MainWindow", "ENTER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
