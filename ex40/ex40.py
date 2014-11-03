#create class
class Song (object):

	#create instantiate function
	def __init__(self, lyrics):
		self.lyrics = lyrics

	#create sing_me_a_song function
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

#instantace an object from this class
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

#instantace an object from this class
bulls_on_parade = Song(["They will rally around tha family",
						"With pockets full of shells"])

#calls function is object
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

