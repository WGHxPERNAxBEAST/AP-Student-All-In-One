import sys
import socket
import time
import json
from PyQt5 import QtWidgets, QtGui, QtCore

def connectSocket():
	port = 8080
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Load in ips which are stored in a gitignored file for security
	with open('Resources/ips.json', 'r') as fp:
		ips = json.load(fp)["ips"]
		fp.close()
	# Repeatedly attempt to connect to each ip until a connection is made
	connState = False
	while not connState:
		for ip in ips:
			try:
				s.connect((ip["addr"], port))
				connState = True
				print(f'Connection Successful on {ip["name"]}')
				break
			except:
				print(f'Cannot connect to {ip["name"]}')
				time.sleep(0.5)
	return s

# ins = [Label content, Input type, Optional third input]
def makeForm(self, ins):
	form = dict()
	form["Questions"] = []
	for inp in ins:
		q = inp[0]
		inType = inp[1]
		#Optional third input
		try:
			thirdIn = inp[2]
		except:
			thirdIn = None
		line = dict()
		line["Q"] = q
		line["TYPE"] = inType
		line["LAB"] = QtWidgets.QLabel(q)
		if inType == "LE": #Line Edit
			line["IN"] = QtWidgets.QLineEdit(self)
			# LE third input is a regexp (Regular Expression)
			if thirdIn is not None:
				line["IN"].setValidator(QtGui.QRegExpValidator(QtCore.QRegExp(thirdIn)))
		elif inType == "DD": #Drop Down
			line["IN"] = QtWidgets.QComboBox(self)
			if thirdIn is not None:
				line["IN"].addItem("Select an option")
				for option in thirdIn:
					line["IN"].addItem(option)
		form["Questions"].append(line)
	return form


def buildFormLayout(form):
	formVBox = QtWidgets.QVBoxLayout()
	formVBox.addStretch()
	for line in form["Questions"]:
		lineHbox = QtWidgets.QHBoxLayout()
		lineHbox.addStretch()
		lineHbox.addWidget(line["LAB"])
		lineHbox.addWidget(line["IN"])
		lineHbox.addStretch()
		formVBox.addLayout(lineHbox)
	formVBox.addStretch()
	formHbox = QtWidgets.QHBoxLayout()
	formHbox.addLayout(formVBox)
	return formHbox