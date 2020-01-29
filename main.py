import os
import sys
import inspect
from PyQt5 import QtWidgets

import Screens

app = QtWidgets.QApplication(sys.argv)

HOME_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


with open('PyQt5StyleSheet.css', 'r') as styleSheet:
	qss = styleSheet.read()
	app.setStyleSheet(qss)
homeWin = Screens.homeScreen.HomePage()
homeWin.show()
sys.exit(app.exec_())