from sys import exit

def leveltwo():
	print 'welcome to All In- the game'
	print "You've made it to Level 2!"
	print 'here is your bet for $100'
	bet = input('do you bet(1) or fold(0)?>')


	if bet == 1:
		#replay level functionality
		print 'you lose, try again?'
		again = raw_input("Yes or No? >")

		if again =='yes':
			level()
		if again == 'no':
			exit()

	elif bet == 0:
		print 'nice job you live another round here is $50 more.'
		leveltwo()

	else:
		print "you failed we were looking for a 0 or 1"
		exit()

def start():
	print 'welcome to All In - the game'
	print 'the rules are simple'
	print 'at each level you can select 1 or 0'
	print '1 = you are all in'
	print '0 = you do not bet'
	print 'here is your first bet for $50'
	bet = input("> ")

	if bet == 1:
		print 'you lose, try again'
		exit(0)
	elif bet == 0:
		print 'nice job you live another round here is $50 more.'
		leveltwo()



start()