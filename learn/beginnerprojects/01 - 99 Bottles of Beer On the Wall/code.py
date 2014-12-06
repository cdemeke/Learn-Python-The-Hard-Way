# This code takes a user input for number of beers 
# and creates a loop that prints the song lyrics for 
# '99' bottles of beer on the wall


# collect the user input on the number of beer on the wall to start with
num = raw_input("How many bottles of beer on the wall?")

# convert that input into an integer
countDown = int(num)

#set the counter
i = 0

#while loop runs until the counter is greater than the user input 
while i < int(num):

	if countDown != 1:
		print "%r bottles of beer on the wall" % countDown
		print "\t %r bottles of beer on the wall" % countDown
		print "\t You take one down you pass it around"
		countDown -= 1
		print "\t %r bottles of beer on the wall" % countDown
	else:
		print "Only 1 bottle of beer on the wall"
		print "\t Only 1 last bottle of beer on the wall"
		print "\t You take one down you pass it around"
		print "\t Everyone's knocked out from drinking %s bottles of" % num
		print "\t beer off the wall" 
	print "-" * 46

	#while loop exit trigger 	
	i += 1
