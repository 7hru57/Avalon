"""Game Controls"""

class Navigation(object):
	"""Navigation Controls"""
	def __init__(self):
		self.command = {
			0: '',
			1: 'close_game',
			2: 'main_menu',
            }

		self.prompt = {
			0: "",
			1: "Input '" + self.command[1] + "' to close the game",
			2: "Input '" + self.command[2] + "' to return to main menu.", 
            }

class Validation(object):
	"""Validate user input"""
	def __init__(self):
		self.fish = ''

	def check_ext_cmd(self, selected_item, ext_cmd):
		"""Check if Exit Command is selected"""


	def enum_item_selected(self, selected_item, menu_items, ext_cmd):
		"""Validate selected item of enumerated questions"""