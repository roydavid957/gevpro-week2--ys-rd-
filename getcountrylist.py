#!/usr/bin/python3

import sys
from flag_color import *

class Country():
	
    def __init__(self, country):
        self.country = country
        self.color = FlagColor()
    
    def returner(self):
        return self.country
        return self.color

