"""Current Menu"""

#Modules
import control
import menu

#Classes
nav = control.Navigation()
val = control.Validation()

class EnumeratedMenu(object):
	"""Display a menu"""
	def __init__(self):
		self.selected_menu = menu.MainMenu() #Default Main Menu

	def set_menu(self, menu_id):
		"""Facilitate Menu Selection"""

		#Main Menu
		if menu_id == 1:
			self.selected_menu = menu.MainMenu()

		#Settings Menu
		elif menu_id == 2:
			self.selected_menu = menu.SettingMenu()

		else:
			raw_input("Error: menu/DisplayMenu/set_menu()")

	def menu(self, menu_header, menu_items, ext_cmd):
		"""Print the menu text"""

		#Header
		print(menu_header)

		#Items
		for key, value in menu_items.items():
			print(key + ": " + value)

		#Exit Command
		if ext_cmd != 0:
			print(nav.prompt[ext_cmd])


	def display_menu(self, menu_id):
		"""Menu to dispaly"""

		#Set current menu
		self.set_menu(menu_id)

		#Display current menu
		self.menu(
			menu_header= self.selected_menu.menu_header,
			menu_items= self.selected_menu.menu_items,
			ext_cmd = self.selected_menu.ext_cmd
			)

		#Validate user selection
		user_selection = raw_input()
		val_menu = val.enum_item_selected(
								selected_item= user_selection, 
								menu_items= list(self.selected_menu.menu_items.keys()), 
								ext_cmd = self.selected_menu.ext_cmd
								)


		return val_menu

#dis = EnumeratedMenu()
#dis.display_menu(1)










