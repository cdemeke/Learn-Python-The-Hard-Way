## Animal is-a object (yes, sort of consusing) look at the extra credit
class Animal(object):
	pass

## is-a 
class Dog (Animal):

	def __init__ (self, name):
		## has-a 
		self.name = name

## is a 
class Cat(Animal):

	def __init__(self, name):
		## has-a
		self.name = name

## ??
class Person (object):

	
	def __init__(self,name):
		#has-a
		self.name = name

		##Person has-a pet of some kind
		self.pet = None

## is-a
class Employee(Person):

	def __init__(self, name, salary):
		##??
		super(Employee, self).__init__(name)
		##??
		self.salary = salary

##
class Fish(object):
	pass

## is-a 
class Salmon(Fish):
	pass

## is-a 
class Halibut(Fish):
	pass

## is-a
rover = Dog("Rover")

## is-a
satan = Cat("Satan")

## has-a
mary = Person("Mary")

## is-a
mary.pet = satan

## is-a
frank = Employee("Frank", 120000)

## is-a
frank.pet = rover

## has-a
flipper = Fish()

## has-a
crouse = Salmon()

## has-
harry = Halibut()
