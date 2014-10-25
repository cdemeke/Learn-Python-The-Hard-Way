ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."
# .split -> seperates the items based on the space
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# checks while the lenght of items in stuff is under 10 it loops
while len(stuff) !=10:
	# grabs the last item in the array and reutrn it
	next_one = more_stuff.pop()
	# append -> adds to the  back of the array
	print "Adding: ", next_one
	stuff.append(next_one)
	# prints the # of items/ elements in the array
	print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Lets do some thing with stuff"

#prints the second item
print stuff[1]
# prints the last item 
print stuff[-1]
# grabs the last item and return it
print stuff.pop()
# Concatenate and addes a ' ' to space out the words
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # suer stellar!
