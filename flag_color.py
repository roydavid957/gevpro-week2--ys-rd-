#!/usr/bin/python3

import sys
from PyQt4 import QtCore, QtGui
from random import randrange

class FlagColor(QtGui.QColor):
	
	def __init__(self, country):
		super(FlagColor, self).__init__()
		
	def chooseColor(self):
		return(randrange(self.setRed(0, 255)), randrange(self.setGreen(0, 255)), randrange(self.setBlue(0, 255)))
	
if __name__ == '__main__':
	app = QApplication(sys.argv)
	flag_color = FlagColor()
	flag_color.show()
	sys.exit(app.exec_())
