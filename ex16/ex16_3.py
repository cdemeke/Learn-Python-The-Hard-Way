from sys import argv

script, filename = argv 

txt = open(filename)
print "The contents of the file currently are:"
print ""
print "======================================="
print txt.read()
print "======================================="
print ""
print "We're going to erase %r" % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

linebreak = '\n'
re_write = "%s %s %s %s %s %s" % (line1, linebreak, line2, linebreak, line3, linebreak)
target.write(re_write)

print "And finally, we close it. "
target.close()
