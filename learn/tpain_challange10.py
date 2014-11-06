class BaseCharacter(object):
	def __init__(self,name, type):
		self.name = name
		self.type = type

	#prints the name input
	def printName (self):
		print ""
		print "**" * 25
		print "Character name is: %s" % (self.name)
		print "They are %s type of character" % (self.type)

class Weapon(object):
	def Start_Weapon(self):
		self.StartWeapon = True

	def PrintStart_Weapon(self):
		print "You start with a Weapon? %r" %self.StartWeapon

	def EnemyAttack(self):
		self.attackDamage = 5

	def PrintEnemyAttack(self):	
		print "you start with %r attack list" % self.attackDamage




class NPC (BaseCharacter):
	def __init__(self, name, type):
		# access constructor of BaseCharacter
		super(NPC,self).__init__(name, type)

class Enemy (NPC, Weapon):
	def __init__(self,name):
		type = "Enemy"
		super(Enemy,self).__init__(name, type)
		super(Enemy,self).EnemyAttack()


		

class Friendly (NPC):
	def __init__(self, name):
		type = "Friendly"
		super(Enemy,self).__init__(name,type)

class PC (BaseCharacter, Weapon):
	def __init__(self, name, type):
		super(PC, self).__init__(name, type)
		super(PC, self).Start_Weapon()


class Archer (PC):
	def __init__(self, name):
		type = "Archer"
		super(Archer, self).__init__(name, type)

class Butcher(PC):
	def __init__(self, name):
		type = "Butcher"
		super(Butcher, self).__init__(name, type)

class GreenLantern(PC):
	def __init__(self, name):
		type = "Green Lantern"
		super(GreenLantern, self).__init__(name, type)



a = Butcher('Chris')
a.printName()
a.PrintStart_Weapon()

b = Enemy('Jasmine')
b.printName()
b.PrintEnemyAttack()




