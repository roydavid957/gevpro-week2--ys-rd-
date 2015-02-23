#!/usr/bin/env python

from flag_color import *

class Country():

		def __init__(self, country):
			self.country = country
		
		def __str__(self):
			return "Hello from {}".format(self.country)

		
