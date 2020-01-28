import os
import sys
import inspect
from PyQt5 import QtWidgets

from Screens.homeScreen import HomePage

app = QtWidgets.QApplication(sys.argv)

HOME_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


with open('PyQt5StyleSheet.css', 'r') as styleSheet:
	qss = styleSheet.read()
	app.setStyleSheet(qss)
mainWindow = HomePage()
mainWindow.show()
sys.exit(app.exec_())
