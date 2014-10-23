print "Type the filename you'd like to open:"

filename = raw_input("> ")

#sets function open to variable 
txt = open(filename)

#prints the variables file name
print "Here's your file %r:" % filename

#python built in function which prints the contents of the file
print txt.read()

#print statement
print "Type the filename again:"

#sets variable file_again to user prompt
file_again = raw_input("> ")

#sets function open to variable 
txt_again = open(file_again)

#python built in function which prints the contents of the file
print txt_again.read()
