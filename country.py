#!/usr/bin/env python

import sys
from PyQt4 import QtCore, QtGui
from flag_color.py import FlagColor

class Country():
	
	def __init__(self, country):
		self.country = country
		self.initUI
		
	def initUI(self):
		self.combo = QtGui.QComboBox(self)
		self.combo.addItems(self.getCountryList())
		self.combo.move(100,50)
		  
		self.greet = QtGui.QLabel(self)
		self.greet.resize(400,50)
		self.greet.move(110,100)
		  
		self.combo.currentIndexChanged.connect(self.updateUI)
		
		self.frameobj = QtGui.QFrame(self)
		self.redobj = QtGui.QColor(0,0,0)
		self.frameobj.setStyleSheet("QFrame { background-color: %s }" % self.redobj.name())
		self.redobj = flag_color.FlagColor.chooseColor(self.redobj)
		  
		self.frameobj = QtGui.QFrame(self)
		self.greenobj = QtGui.QColor(0,0,0)
		self.frameobj.setStyleSheet("QFrame { background-color: %s }" % self.greenobj.name())
		self.greenobj = flag_color.FlagColor.chooseColor(self.greenobj)
		  
		self.frameobj = QtGui.QFrame(self)
		self.blueobj = QtGui.QColor(0,0,0)
		self.frameobj.setStyleSheet("QFrame { background-color: %s }" % self.blueobj.name())
		self.blueobj = flag_color.FlagColor.chooseColor(self.blueobj)
		  
	def getcountrylist():
		countrylist = []
		with open ('countries_list.txt', 'r') as in_f:
			for line in in_f:
				linelist = line.split()
				countrylist = countrylist + linelist
		return(countrylist)
		  
	def updateUI(self):
		self.country = self.combo.currentText()
		self.greet.setText(self.__str__())
		sttext = "QFrame { background-color: %s }" % flag_color.FlagColor(self.country)
		print(sttext)
		self.setStyleSheet(sttext)
		
	def __str__(self):
		return "Hello from {0}".format(self.country)
  
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	country = Country()
	country.show()
	app.exec_()
