# funtion that takes in two variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket \n"

print "WE can just give the funtion number directly:"
#call function by passing two variables directly
cheese_and_crackers(20,30)

print "Or we can use variables from our script:"
#define each variable 
amount_of_cheese = 10
amount_of_crackers = 50

#call function by passing variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
#call function, but first do math 
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
#call function, by variable name but first do math
cheese_and_crackers(amount_of_crackers + 100, amount_of_cheese + 1000)