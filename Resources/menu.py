"""Menu Display and Menu Items"""
#Libraries
from collections import OrderedDict

class MainMenu(object):
	"""Main Menu"""
	def __init__(self):
		self.menu_header = "Welcome to Avalon! Please select from the following options:"
		self.menu_items = OrderedDict([
									('1', 'Play Game'),
									('2', 'How to Play'),
									('3', 'Settings'),
									('4', 'Leader Board'),
									])
		#Quit Game
		self.ext_cmd = 1

class SettingMenu(object):
	"""Settings Menu"""
	def __init__(self):
		self.menu_header = "Please select a setting to modify:"
		self.menu_items = OrderedDict([
									('1', 'Optional Characters'),
									('2', 'Game Mode'),
									('3', 'Languages'),
									])
		#Main Menu
		self.ext_cmd = 2

class OptionalCharacter(object):
	"""Optional Characters Menu"""
	def __init__(self):
		self.menu_header = "Select the characters you wish to activate:"
		self.menu_items = OrderedDict([
									('1', 'Percival'),
									('2', 'Mordred'),
									('3', 'Morgana'),
									('4', 'Oberon'),
									('5', 'Back to Settings')									
									])
		#Exit Command is in Items
		self.ext_cmd = 0

		#Need to find a way to toggle characters on and off
		




