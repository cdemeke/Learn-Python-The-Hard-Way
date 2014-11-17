#Study Drills
#1 (complete). Convert this while-loop to a function that you can call, and replace 6 in the test (i < 6) with a variable.
#
#2 (complete). Use this function to rewrite the script to try different numbers.
#
#3 (complete). Add another variable to the function arguments that you can pass in that lets you change the + 1 on line 8 so you can change how much it increments by.
#4. Rewrite the script again to use this function to see what effect that has.
#
#5. Write it to use for-loops and range. Do you need the incrementor in the middle anymore? What happens if you do not get rid of it?


# function takes in the user input amount, appends number
# array to that amount and returns the array
def num_while (incement, end):
	i = 0
	number =[]
	# print the incement amount
	print "this is incementing by %d" % incement 

	while i < end:
		# print statement to call what i is before changed
		print "At the top i is %d" % i
		# function to append the array
		number.append(i)

		# increments variable i
		i = i + incement
		# prints the array
		print "Numbers now: ", number
		# print statement to call what i is before changed
		print "At the bottom i is %d" % i
	# return the array
	return number

# prompt the user to input how many times they want the loop to run
user_amount = raw_input("How many times should this run? \n\t:")
#convert the user input %s into an integer
int_user_amount = int(user_amount)

# prompt the user to input how it should incement
user_incement = raw_input("By how many should it increment by? \n\t:")
#convert the user input %s into an integer
int_user_incement = int(user_incement)


#call function num_while passing the user amount and return the array
number = num_while(int_user_incement, int_user_amount)


print "The numbers: "

#for num in number:
#	print num