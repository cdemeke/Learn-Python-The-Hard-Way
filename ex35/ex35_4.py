from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"

	choice = raw_input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice)

	else:
		dead("Man, learn to tpye a number.")

	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastaard!")

def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey"
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		choice = raw_input("> ")

		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now"
			bear_moved = True

		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your lef off.")

		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."



def monsters_inc():
	print "you are transported in to Monsters Inc"
	print "You are asked if you'd like to:"
	print "1. Scare a Kid"
	print "2. Scare an Adult"
	print "3. Scare an Old Person"
	
	scare = int(raw_input("> "))
	
	if scare == 1:
		print "Nice job the kid is terrified!"
		exit(0)

	elif scare == 2:
		dead("The Adult isn't scared and you get arrested for breaking and entering")

	elif scare == 3:
		dead("The Old Person isn scared to death and you get arrested for... MURDER")

	else:
		print "you fall into an unknown door and..."
		monsters_inc()


def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat y our head?"

	choice = raw_input("> ")

	if "flee" in choice:
		monsters_inc()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"

	choice = raw_input("> ")

	if choice == "left" :
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else: 
		dead("You stumble around the room until you starve.")

start()