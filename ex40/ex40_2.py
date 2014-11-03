class Song (object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They will rally around tha family",
						"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


linebreak = Song(["-----------------------------------------------"])

mary_text = "Mary had a little lamb."
lamb_text = ['Little Lamb, little lamb.'' And everywhere that Mary went, the lamb was sure to go']

mary_lamb = Song([mary_text])

#','.join takes all the elemnts of the list and joins them w/ ','
little_lamb = Song ([','.join(lamb_text)])

linebreak.sing_me_a_song()
mary_lamb.sing_me_a_song()
little_lamb.sing_me_a_song()