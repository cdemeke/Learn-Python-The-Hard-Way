from Base import * 

class inClass (BaseClass):

	def __init__(self):
		self.x = 17


class inClassAgain (BaseClass):

	def printHam(self):
		print "Ham2"

class inClassFinal (inClass, inClassAgain):

	def __init__(self):
		print "hey"
		super(inClassFinal,self).__init__(x)
		print self.x
		super(inClassFinal,self).printHam()





#Test
#x = inClass()
#print x.x
#y = inClassAgain()
#y.printHam()

#z = inClassFinal()

print BaseClass.__subclasses__()
print inClass.__subclasses__()