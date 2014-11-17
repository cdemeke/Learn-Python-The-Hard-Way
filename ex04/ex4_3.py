#this defines the cars
cars = 100
#this defins the seats in a car
space_in_a_car = 4.0
#this defines the # of drivers available
drivers = 30
#this defines the # of passangers that need rides
passengers = 90
#this calculates the number of cars that will not be driven
cars_not_driven = cars - drivers
#this maps cars availabe to # of drivers
cars_driven = drivers
#this calculates the # of total seats in all the driving cars
carpool_capacity = cars_driven * space_in_a_car
#this calculates the ~est number of passangers per car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers,"drivers available"
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car."