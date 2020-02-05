from PyQt5 import QtWidgets, QtGui, QtCore

import Resources.pyqt5Helper as helper
import Screens

class LogInPage(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.s = helper.connectSocket()
		self.init_ui()

	def init_ui(self):
		self.TitleLab = QtWidgets.QLabel('Log-In!')
		self.submitBtn = QtWidgets.QPushButton('Submit')
		self.cancelBtn = QtWidgets.QPushButton('Cancel')
		#	["Q", "TYPE", "REGEXP"] REGEXP is optional
		formIn = [
			["Username", "LE", "[a-z_A-Z0-9]{1,20}"],
			["Password", "LE", "[a-z_A-Z0-9]{1,20}"]
		]
		self.form = helper.makeForm(self, formIn)
		self.form["Questions"][1]["IN"].setEchoMode(QtWidgets.QLineEdit.Password)
		self.ErrorLab = QtWidgets.QLabel()
		self.singUpPageLayout()

		self.setWindowTitle('AIO AP Student Resource - Log In')

		self.submitBtn.clicked.connect(self.submit)
		self.cancelBtn.clicked.connect(self.cancel)


	def singUpPageLayout(self):
		titleHbox = QtWidgets.QHBoxLayout()
		titleHbox.addStretch()
		titleHbox.addWidget(self.TitleLab)
		titleHbox.addStretch()

		buttonsHbox = QtWidgets.QHBoxLayout()
		buttonsHbox.addStretch()
		buttonsHbox.addWidget(self.cancelBtn)
		buttonsHbox.addStretch()
		buttonsHbox.addWidget(self.submitBtn)
		buttonsHbox.addStretch()

		errorHbox = QtWidgets.QHBoxLayout()
		errorHbox.addStretch()
		errorHbox.addWidget(self.ErrorLab)
		errorHbox.addStretch()

		v_box = QtWidgets.QVBoxLayout()
		v_box.addStretch()
		v_box.addLayout(titleHbox)
		v_box.addStretch()
		v_box.addLayout(helper.buildFormLayout(self.form))
		v_box.addStretch()
		v_box.addLayout(buttonsHbox)
		v_box.addStretch()
		v_box.addStretch()
		v_box.addLayout(errorHbox)
		v_box.addStretch()

		self.setLayout(v_box)

	def submit(self):
		self.s.send(b"\x11" + self.form["Questions"][1]["IN"].text())
		SignInResponse = self.s.recv(2048)
		self.s.send(b"\x12" + self.form["Questions"][2]["IN"].text())
		SignInResponse = self.s.recv(2048)
		self.s.send(b"\x13")
		SignInResponse = self.s.recv(2048)
		if (SignInResponse != "Password Failed") & (SignInResponse != "Failed"):
			self.advanceScreen()
		elif SignInResponse == "Password Failed":
			self.ErrorLab.setText("Your password is incorrect")
			self.form["Questions"][2]["IN"].clear()
		else:
			self.ErrorLab.setText("Your username is invalid")
			self.form["Questions"][2]["IN"].clear()

	def cancel(self):
		self.s.close()
		self.homeWin = Screens.homeScreen.HomePage()
		self.homeWin.show()
		self.close()

	def advanceScreen(self):
		self.s.close()
		self.viewClassesWin = Screens.viewClassesScreen.ViewClassesPage()
		self.viewClassesWin.show()
		self.close()
