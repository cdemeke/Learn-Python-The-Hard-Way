#created the array
numbers = []

#function while_loop_function, expecting the passed count variable and incement variable
def while_loop_function (count, i):
	
	#started while loop
	while i < count:
	    print "At the top i is %d" % i
	    numbers.append(i)

	    i = i + 2
	    print "Numbers now: ", numbers
	    print "At the bottom i is %d" % i

#sets the count variable 
count_variable = raw_input ("How many variables should I count up to? :")

#sets 2ns variable incement
incement = raw_input("By how many numbers should the script incement by? :")
#calls the function and passes the count variable
#had to use the int function to turn the user input into integers
while_loop_function(int(count_variable), int(incement))

print "The numbers: "

for num in numbers:
    print num