while True:


	import random


	__title__ = 'Life Simulator'
	__version__ = '0.0.1'
	__author__ = 'Freddy Pashley'
	__license__ = 'MIT'
	__notes__ = 'This is the main script used for Life Simulator.'



	print('\nWelcome to Life Simulator!\n\nThis is a text-based simulator designed to be an arcade-style game where you can live any life you wish.\n\nGood luck!\nPlease note that all of your answers are not case-sensitive, however they must be recognised by the game as an answer to be valid. Otherwise, you risk losing your progress. All valid answers are displayed when needed.\n\n\n')

	def new_game():
		ready = input('Are you ready to start? (Y/N) - ')
		if ready.lower() == 'y':
			print('Starting.')
		else:
			pass


	new_game()