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
			1: "Input '" + self.command[1] + "' to close the game.",
			2: "Input '" + self.command[2] + "' to return to main menu.", 
            }

	def print_or_prompt(self, ext_cmd):
		"""Begin prompt with 'Or' """
		print("Or " + self.prompt[ext_cmd][0].lower() + self.prompt[ext_cmd][1:])


class Validation(object):
	"""Validate user input"""
	def __init__(self):
		self.nav = Navigation()

	def enum_item_selected(self, selected_item, menu_items, ext_cmd):
		"""Validate selected item of enumerated questions"""
		self.valid = False 												#Set Default Flag

		while self.valid == False:

			#Check for Exit Command
			if selected_item in self.nav.command.values()[1:]:
				self.valid = True										#Valid Exit Command

			#Validate Response
			else:

				#Valid
				if selected_item in menu_items:
					self.valid = True	

				#Invalid
				else:
					print("Please select an item from the list above.")	#Loop error message
					self.nav.print_or_prompt(ext_cmd)

					selected_item = raw_input()							#New user selection

		#Return Valid Item
		return selected_item









