#!/usr/bin/env python

from PyQt import QtCore, QtGui
from random import randrange

class FlagColor(QtGui.QColor):
	
	def __init__(self, country):
		super(FlagColor, self).__init__()
		self.initUI
		
	def initUI(self):
		self.country = country
		self.color = self.chooseColor()
		
	def chooseColor(self):
		return(randrange(self.setRed(0, 255)), randrange(self.setGreen(0, 255)), randrange(self.setBlue(0, 255)))
