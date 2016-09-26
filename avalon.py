"""Created by: Michael Lee
   Created on: 2016-09-22
   Python Version: 2.7
   Description: A game of hidden Loyalties"""

#Absolute File Path to Resources Directory
import sys, os
afp = os.path.dirname(os.path.abspath(__file__)) + '/Resources/'
sys.path.append(afp)

#Modules
import control
import menu_control
how_to_play = afp + 'how_to_play.txt'

#Classes
nav = control.Navigation()
menu = menu_control.EnumeratedMenu()

#Flag
game_active = True

#Game
while game_active == True:

	#Display Main Menu
	selected_menu = menu.display_menu(menu_id= 1)
	#selected_menu = 2

	#If Selected Menu is not close game
	if selected_menu != nav.command[1]:

		#Play Game
		if selected_menu == 1:
			print("1")

		#How to Play
		elif selected_menu == 2:

			#Read how_to_play.txt 
			with open(how_to_play) as file_object:
				contents = file_object.read()
				print(contents)

			raw_input("Press the enter key to return to the Main Menu.")
			game_active = False #Kill game

		#Settings
		elif selected_menu == 3:

			#Display Setting Menu
			selected_setting = menu.display_menu(menu_id= 2)

			#Not built yet
			if selected_setting not in nav.command.values():
				if selected_setting == 1:
					print('Optional Characters')
				elif selected_setting == 2:
					print('Game Mode')
				elif selected_setting == 3:
					print('Languages')
				else:
					raw_input("You dun' broke it")

		#Leaderboard
		elif selected_menu == 4:
			print("2")

		else:
			raw_input("You're tearin' up my heart when I'm with you~")
			game_active = False

	#End Game
	else:
		game_active = False

