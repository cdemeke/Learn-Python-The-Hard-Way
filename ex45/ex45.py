##########################################################
# This is a rock paper sissors game
# The objective of the game is as follows
#  1.  The user enters the # of games they'd like to play.
#  2.  The user is requested to input their guess 'rock' 'paper' 'sissors'.
#  3.  The computer generates a random value from a list as it's guess.
#  4.  The Calculate method in CalculateWinner will determine which guess wins.
#  5.  The game loops over again until it meets the user input of # of games @ step  1.
##########################################################

import random

class RockPaperSissorsEngine (object):
	"""
	This is the main engine for the game.
	"""

	def __init__(self):
		count = self.NumOfGames() # request how many games the user will like to play
		self.play(count)
		
	def play(self, count):
		# sets number of games counter
		i = 0 
		# sets the win count
		wins = 0

		#  sets loop for the number of games the user will like to play
		while i < count:

			print "-" * 40

			# add to the # of games played counter
			i += 1
			
			# track the number of games
			print "This is game #  %d out of %d" % (i, count)
			
			# instantiate CalculateWinner class
			self.request = CalculateWinner()

			# get user input 
			userInput = self.request.UserInput()

			# get computer input
			computerInput = self.request.ComputerInput() 
			print "\t The CPU guessed: %r" % computerInput

			# pass user input and computer input to calcuate result
			result = self.request.Calculate(userInput,computerInput)
			
			#incremental add to win count 
			wins += result 
		
		# print results
		print "\n" * 2
		print "=" * 40
		print "Out of the %r game(s) your played, you won %r" % (count, wins)

	def NumOfGames(self):
		print "How many games would you like to play?"
		count = raw_input("> ")
		# return user request # of games
		return int(count)


class CalculateWinner (object):

	def UserInput (self):
		"""
		Capture user input.
		"""		
		print "Please enter your choice of 'Rock', 'Paper', Sissors'"
		userInput = raw_input("\t Your guess:")
		# convert to upper case
		userInput = userInput.upper() 

		if (userInput == 'ROCK') or (userInput == 'PAPER') or (userInput == 'SISSORS') :
			pass

		else:
		# check to make sure valid input was entered
			validValue = False 

			# lopp until user enters correct input
			while validValue != True:
				print "-" * 40
				print "\t Unrecognized input"
				print "\t Please enter 'Rock', 'Paper', Sissors'"
				# user input again
				userInput = raw_input("\t Your guess:")
				userInput = userInput.upper()

				# checks if user input is acceptable
				if (userInput == 'ROCK') or (userInput == 'PAPER') or (userInput == 'SISSORS') :
					# loop exit trigger
					validValue = True
				else:
					pass
		
		return userInput

	def ComputerInput(self):
		"""
		Generate the computer random guess.
		"""
		inputs = ['Rock', 'Paper', 'Sissors']
		ComputerInput = (random.choice(inputs))
		# convert to upper case
		ComputerInput = ComputerInput.upper()
		return ComputerInput


	def Calculate(self, userInput, computerInput):
		"""
		Calculates the types of situations for rock paper sissors.
		"""
		if userInput == computerInput:
			print "TIE"
			return 0

		elif (userInput == 'ROCK' and computerInput == 'Paper') or (userInput == 'PAPER' and computerInput == 'SISSORS') or (userInput == 'SISSORS' and computerInput == 'ROCK'):
			print "Computer Wins"
			return -1

		else:
			print "You Win"
			return +1

game = RockPaperSissorsEngine()
