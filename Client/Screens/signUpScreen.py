import json
from PyQt5 import QtWidgets, QtGui, QtCore

import Resources.pyqt5Helper as helper
import Screens

class SignUpPage(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.s = helper.connectSocket()
		self.init_ui()

	def init_ui(self):
		self.TitleLab = QtWidgets.QLabel('Sign-Up!')
		self.submitBtn = QtWidgets.QPushButton('Submit')
		self.cancelBtn = QtWidgets.QPushButton('Cancel')
		#	["Label", "TYPE", Optional third (REGEXP or Option list)]
		formIn = [
			["Email", "LE", "([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})"],
			["Username", "LE", "[a-z_A-Z0-9]{1,20}"],
			["Password", "LE", "[a-z_A-Z0-9]{1,20}"],
			["Grade", "DD", ["8","9","10","11","12"]],
			["GPA", "LE", "[0-5]{1}\.\d*"],
			["Sex", "DD", ["Male", "Female", "Other"]],
			["Age", "LE", "[1-2]{1}[0-9]{1}"]
		]
		self.form = helper.makeForm(self, formIn)
		self.form["Questions"][2]["IN"].setEchoMode(QtWidgets.QLineEdit.Password)
		self.singUpPageLayout()

		self.setWindowTitle('AIO AP Student Resource - Sign Up')

		self.submitBtn.clicked.connect(self.submit)
		self.cancelBtn.clicked.connect(self.cancel)


	def singUpPageLayout(self):
		titleHbox = QtWidgets.QHBoxLayout()
		titleHbox.addStretch()
		titleHbox.addWidget(self.TitleLab)
		titleHbox.addStretch()

		buttonsHbox = QtWidgets.QHBoxLayout()
		buttonsHbox.addStretch()
		buttonsHbox.addWidget(self.submitBtn)
		buttonsHbox.addStretch()
		buttonsHbox.addWidget(self.cancelBtn)
		buttonsHbox.addStretch()

		v_box = QtWidgets.QVBoxLayout()
		v_box.addStretch()
		v_box.addLayout(titleHbox)
		v_box.addStretch()
		v_box.addLayout(helper.buildFormLayout(self.form))
		v_box.addStretch()
		v_box.addLayout(buttonsHbox)
		v_box.addStretch()

		self.setLayout(v_box)

	def submit(self):
		user = dict()
		for q in self.form["Questions"]:
			if q["TYPE"] == "LE":
				user[q["Q"]] = q["IN"].text()
			elif q["TYPE"] == "DD":
				user[q["Q"]] = q["IN"].currentText()
		self.s.send(b"\x14" + bytes(json.dumps(user),'utf-8'))
		response = self.s.recv(2048)
		self.stage2()

	def stage2(self):
		self.s.close()
		self.stage2Win = SignUpPage2()
		self.stage2Win.show()
		self.close()

	def cancel(self):
		self.s.close()
		self.homeWin = Screens.homeScreen.HomePage()
		self.homeWin.show()
		self.close()

class SignUpPage2(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.s = helper.connectSocket()
		self.init_ui()

	def init_ui(self):
		self.TitleLab = QtWidgets.QLabel('Sign-Up!')
		self.submitBtn = QtWidgets.QPushButton('Submit')
		self.cancelBtn = QtWidgets.QPushButton('Cancel')
		self.qLab = QtWidgets.QLabel('Select all AP Classes you are currently taking:')
		self.classList = self.makeClassList()
		self.singUpPage2Layout()

		self.setWindowTitle('AIO AP Student Resource - Sign Up')

		self.submitBtn.clicked.connect(self.submit)
		self.cancelBtn.clicked.connect(self.cancel)


	def singUpPage2Layout(self):
		titleHbox = QtWidgets.QHBoxLayout()
		titleHbox.addStretch()
		titleHbox.addWidget(self.TitleLab)
		titleHbox.addStretch()

		title2Hbox = QtWidgets.QHBoxLayout()
		title2Hbox.addStretch()
		title2Hbox.addWidget(self.qLab)
		title2Hbox.addStretch()

		buttonsHbox = QtWidgets.QHBoxLayout()
		buttonsHbox.addStretch()
		buttonsHbox.addWidget(self.submitBtn)
		buttonsHbox.addStretch()
		buttonsHbox.addWidget(self.cancelBtn)
		buttonsHbox.addStretch()

		v_box = QtWidgets.QVBoxLayout()
		v_box.addStretch()
		v_box.addLayout(titleHbox)
		v_box.addStretch()
		v_box.addLayout(title2Hbox)
		v_box.addLayout(self.buildCheckBoxListLayout())
		v_box.addStretch()
		v_box.addLayout(buttonsHbox)
		v_box.addStretch()

		self.setLayout(v_box)

	def makeClassList(self):
		apClassNames = ["Chem", "Physics", "Lang", "Java", "CS Principles", "World"]
		apClasses = []
		for apClassName in apClassNames:
			apClass = dict()
			apClass["name"] = apClassName
			apClass["box"] = QtWidgets.QCheckBox(apClassName)
			apClasses.append(apClass)
		return apClasses

	def buildCheckBoxListLayout(self):
		vBox = QtWidgets.QVBoxLayout()
		vBox.addStretch()
		for apClass in self.classList:
			vBox.addWidget(apClass["box"])
		vBox.addStretch()
		hBox = QtWidgets.QHBoxLayout()
		hBox.addStretch()
		hBox.addLayout(vBox)
		hBox.addStretch()
		return hBox

	def submit(self):
		for apClass in self.classList:
			apClass["box"] = apClass["box"].checkState()
		self.s.send(b"\x15" + bytes(json.dumps(self.classList),'utf-8'))
		response = self.s.recv(2048)
		self.s.send(b"\x16")
		response = self.s.recv(2048)
		self.advance()

	def advance(self):
		self.s.close()
		self.viewClassesWin = Screens.viewClassesScreen.ViewClassesPage()
		self.viewClassesWin.show()
		self.close()

	def cancel(self):
		self.s.close()
		self.homeWin = Screens.homeScreen.HomePage()
		self.homeWin.show()
		self.close()