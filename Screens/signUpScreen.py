from PyQt5 import QtWidgets, QtGui, QtCore

class signUpPage(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.TitleLab = QtWidgets.QLabel('Sign-Up!')
		self.submitBtn = QtWidgets.QPushButton('Submit')
		self.cancelBtn = QtWidgets.QPushButton('Cancel')
		formIn = [
			("Email", "([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})"),
			("Username", "[a-z_A-Z0-9]{1,20}"),
			("Password", "[a-z_A-Z0-9]{1,20}"),
			("Grade", "[0-9]{1,2}"),
			("GPA", "\d\.\d*"),
			("Sex(M/F)", "([M][F]){1}"), #REGEX Broken
			("Age", "[0-9]{1,2}")
		]
		self.form = self.makeForm(formIn)
		self.singUpPageLayout()

		self.setWindowTitle('AIO AP Student Resource - Sign Up')


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
		v_box.addLayout(self.buildFormLayout(self.form))
		v_box.addStretch()
		v_box.addLayout(buttonsHbox)
		v_box.addStretch()

		self.setLayout(v_box)

	def makeForm(self, ins=[("Q", "REGEXP")]):
		form = dict()
		form["Questions"] = []
		for inp in ins:
			q = inp[0]
			regexp = inp[1]
			line = dict()
			line["Q"] = q
			line["LAB"] = QtWidgets.QLabel(q)
			line["LE"] = QtWidgets.QLineEdit(self)
			line["LE"].setValidator(QtGui.QRegExpValidator(QtCore.QRegExp(regexp)))
			form["Questions"].append(line)
		return form

	def buildFormLayout(self, form=dict()):
		formVBox = QtWidgets.QVBoxLayout()
		formVBox.addStretch()

		for line in form["Questions"]:
			lineHbox = QtWidgets.QHBoxLayout()
			lineHbox.addStretch()
			lineHbox.addWidget(line["LAB"])
			lineHbox.addWidget(line["LE"])
			lineHbox.addStretch()
			formVBox.addLayout(lineHbox)
		formVBox.addStretch()
		formHbox = QtWidgets.QHBoxLayout()
		formHbox.addLayout(formVBox)
		return formHbox

