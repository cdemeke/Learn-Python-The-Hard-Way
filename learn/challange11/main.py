class BaseClass (object):

	def __init__(self):
		self.x = 5

	def printHam(self):
		print "Ham"


x = BaseClass()
x.printHam()
print x.x