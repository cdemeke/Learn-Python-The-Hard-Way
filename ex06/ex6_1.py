#sets the value for x and also defines %d as '10'
x = "There are %d types of people" % 10
#sets the value for binary
binary = "binary"
#sets the value for do_not
do_not = "don't"

#sets the value for y which includes variable binary & do_not
y = "Those who know %s and those who %s" % (binary, do_not)

#prints x
print x

#prints y
print y

#prints x w/ prepend '%r' = raw (aka the value as what python sees it as)
print "I said: %r." % x

#prints y w/ prepend 
print "I also said: '%s'." % y

#sets hilarious
hilarious = False

#sets joke_evaluation /w a value input
joke_evaluation = "isn't that joke so funny?! %r"

#prints joke_evaluation + the value input as variable hilarious
print joke_evaluation % hilarious

#sets w
w = "This is the left side of..."
#sets e
e = "a string with a right side."

#prints w + e
print w + e