import sys
import socket
import time
from PyQt5 import QtWidgets, QtGui, QtCore

def connectSocket():
	port = 8080
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	with open('ips.json', 'r+') as fp:
		ips = json.load(fp)["ips"]
		fp.close()
	connState = False
	while connState == False:
		for ip in ips:
			try:
				s.connect((ip["addr"], port))
				connState = True
				print(f'Connection Successful on {ip["name"]}')
			except:
				print(f'Cannot connect to {ip["name"]}')
				time.sleep(0.5)
	return s

def makeForm(self, ins):
	form = dict()
	form["Questions"] = []
	for inp in ins:
		q = inp[0]
		inType = inp[1]
		try:
			regexp = inp[2]
		except:
			regexp = "None"
		line = dict()
		line["Q"] = q
		line["LAB"] = QtWidgets.QLabel(q)
		if inType == "LE":
			line["IN"] = QtWidgets.QLineEdit(self)
			if regexp != "None":
				line["IN"].setValidator(QtGui.QRegExpValidator(QtCore.QRegExp(regexp)))
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