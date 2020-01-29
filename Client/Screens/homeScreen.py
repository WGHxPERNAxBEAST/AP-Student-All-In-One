from PyQt5 import QtWidgets, QtGui, QtCore

import Resources.pyqt5Helper as helper
import Screens

class HomePage(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.TitleLab = QtWidgets.QLabel('Welcome to the All In One AP Student Resource')
		self.logInBtn = QtWidgets.QPushButton('Log In')
		self.signUpBtn = QtWidgets.QPushButton('Sign Up')

		self.homepageLayout()

		self.setWindowTitle('AIO AP Student Resource')

		self.logInBtn.clicked.connect(self.logIn)
		self.signUpBtn.clicked.connect(self.signUp)

	def homepageLayout(self):
		titleHbox = QtWidgets.QHBoxLayout()
		titleHbox.addStretch()
		titleHbox.addWidget(self.TitleLab)
		titleHbox.addStretch()

		buttonsHbox = QtWidgets.QHBoxLayout()
		buttonsHbox.addStretch()
		buttonsHbox.addWidget(self.logInBtn)
		buttonsHbox.addStretch()
		buttonsHbox.addWidget(self.signUpBtn)
		buttonsHbox.addStretch()

		v_box = QtWidgets.QVBoxLayout()
		v_box.addStretch()
		v_box.addLayout(titleHbox)
		v_box.addStretch()
		v_box.addLayout(buttonsHbox)
		v_box.addStretch()

		self.setLayout(v_box)

	def logIn(self):
		self.logInWin = Screens.logInScreen.LogInPage()
		self.logInWin.show()
		self.close()

	def signUp(self):
		self.signUpWin = Screens.signUpScreen.SignUpPage()
		self.signUpWin.show()
		self.close()