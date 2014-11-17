#created the array
numbers = []

#function while_loop_function, expecting the passed count variable
def while_loop_function (count):
	
	i = 0
	#started while loop
	while i < count:
	    print "At the top i is %d" % i
	    numbers.append(i)

	    i = i + 2
	    print "Numbers now: ", numbers
	    print "At the bottom i is %d" % i

#sets the count variable 
count_variable = 20

#calls the function and passes the count variable
while_loop_function(count_variable)

print "The numbers: "

for num in numbers:
    print num