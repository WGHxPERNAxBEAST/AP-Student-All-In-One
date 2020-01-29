from PyQt5 import QtWidgets, QtGui, QtCore

import Resources.pyqt5Helper as helper
import Screens

class SignUpPage(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.TitleLab = QtWidgets.QLabel('Sign-Up!')
		self.submitBtn = QtWidgets.QPushButton('Submit')
		self.cancelBtn = QtWidgets.QPushButton('Cancel')
		#	["Q", "TYPE", "REGEXP"] REGEXP is optional
		formIn = [
			["Email", "LE", "([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})"],
			["Username", "LE", "[a-z_A-Z0-9]{1,20}"],
			["Password", "LE", "[a-z_A-Z0-9]{1,20}"],
			["Grade", "LE", "[0-9]{1,2}"],
			["GPA", "LE", "\d\.\d*"],
			["Sex(M/F)", "LE", "([M],[F]){1}"], #REGEX Broken
			["Age", "LE", "[0-9]{1,2}"]
		]
		self.form = helper.makeForm(self, formIn)
		self.singUpPageLayout()

		self.setWindowTitle('AIO AP Student Resource - Sign Up')

		self.submitBtn.clicked.connect(self.stage2)
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

	def stage2(self):
		self.stage2Win = SignUpPage2()
		self.stage2Win.show()
		self.close()

	def cancel(self):
		self.homeWin = Screens.homeScreen.HomePage()
		self.homeWin.show()
		self.close()

class SignUpPage2(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.TitleLab = QtWidgets.QLabel('Sign-Up!')
		self.submitBtn = QtWidgets.QPushButton('Submit')
		self.cancelBtn = QtWidgets.QPushButton('Cancel')
		self.qLab = QtWidgets.QLabel('Select all AP Classes you are currently taking:')
		self.classList = self.makeClassCbList()
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
		v_box.addLayout(self.buildCheckBoxListLayout(self.classList))
		v_box.addStretch()
		v_box.addLayout(buttonsHbox)
		v_box.addStretch()

		self.setLayout(v_box)

	def makeClassCbList(self):
		apClasses = ["Chem", "Physics", "Lang", "Java", "CS Principles", "World"]
		checkBoxes = []
		for apClass in apClasses:
			checkBoxes.append(QtWidgets.QCheckBox(apClass))
		return checkBoxes

	def buildCheckBoxListLayout(self, checkBoxes):
		vBox = QtWidgets.QVBoxLayout()
		vBox.addStretch()
		for box in checkBoxes:
			vBox.addWidget(box)
		vBox.addStretch()
		hBox = QtWidgets.QHBoxLayout()
		hBox.addStretch()
		hBox.addLayout(vBox)
		hBox.addStretch()
		return hBox

	def submit(self):
		self.viewClassesWin = Screens.viewClassesScreen.ViewClassesPage()
		self.viewClassesWin.show()
		self.close()

	def cancel(self):
		self.homeWin = Screens.homeScreen.HomePage()
		self.homeWin.show()
		self.close()