#!/usr/bin/env python
#Youri Schuur & Roy David
#Youri kon niks pushen door permissies waar we niet uitkwamen dus hebben we het samen op mijn pc gedaan

import sys
from PyQt4 import QtCore, QtGui
from getcountrylist import *
from flag_color import *
from random import randrange

def getcountrylist(stdin):
    countrieslist = []
    countrieslist1 = []
    for line in sys.stdin:
        linelist = line.strip()
        country1 = Country(line)
        countrieslist.append(country1)
        countrieslist1.append(linelist)
    return countrieslist1
    
def randomnumber():
	return randrange(0, 255), randrange(0, 255), randrange(0, 255)

class Country(QtGui.QWidget):
	
	def __init__(self):
		super(Country, self).__init__()
		self.initUI
		
	def initUI(self):
		self.combo = QtGui.QComboBox(self)
		self.combo.move(100,50)
		countrynames = getcountrylist(self)
		self.combo.addItems(sorted(countrynames))
		self.combo.currentIndexChanged.connect(self.updateUI)
		
		self.frame1 = QtGui.QFrame(self)
		self.color1 = QtGui.QColor(0,0,0)
		self.frame1.setStyleSheet("QFrame { background-color: %s }" % self.color1.name())
		self.frame1.setGeometry(50, 90, 240, 30)
		  
		self.frame2 = QtGui.QFrame(self)
		self.color2 = QtGui.QColor(0,0,0)
		self.frame2.setStyleSheet("QFrame { background-color: %s }" % self.color2.name())
		self.frame2.setGeometry(50, 90, 240, 30)
		  
		self.frame3 = QtGui.QFrame(self)
		self.color3 = QtGui.QColor(0,0,0)
		self.frame3.setStyleSheet("QFrame { background-color: %s }" % self.color3.name())
		self.frame3.setGeometry(50, 90, 240, 30)
		
		self.setGeometry(350, 350, 350, 200)
		self.setWindowTitle("Flags")
		self.show()
		  
	def updateUI(self):
		col1, col2, col3 = randomnumber()
		col11, col21, col31 = randomnumber()
		col12, col22, col32 = randomnumber()
		self.color1 = QtGui.QColor(col1, col2, col3)
		self.color2 = QtGui.QColor(col11, col21, col31)
		self.color3 = QtGui.QColor(col12, col22, col32)
		self.frame1.setStyleSheet("QWidget { background-color: %s }" % self.color1.name())
		self.frame2.setStyleSheet("QWidget { background-color: %s }" % self.color2.name())
		self.frame3.setStyleSheet("QWidget { background-color: %s }" % self.color3.name())
  
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	country = Country()
	sys.exit(app.exec_())
