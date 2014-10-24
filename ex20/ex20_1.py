#imports argv method
from sys import argv

#defines the variables input from the command line
script, input_file = argv

#funtion takes in file name
def print_all (f):
	print f.read()
#function starts from the beginning of the document
def rewind(f):
	f.seek(0)
#function takes in line # and file name to print out whats on that line
def print_a_line (line_count, f):
	print line_count, f.readline(),

#opens that file
current_file = open(input_file)


print "First let's print the whole file:\n"
#calls function to print all the file contents
print_all(current_file)

print "Now let's rewint, kind of like a tape."
#calls the rewind function to start from the top again
rewind(current_file)

print "Let's print three lines:"
#sets current line
current_line = 1
#calls print function at line 1
print_a_line(current_line, current_file)

#sets the line of the file to 2
current_line += 1
#calls print function at line 2
print_a_line(current_line, current_file)

#sets the line of the file to 3
current_line += 1
#calls print function at line 3
print_a_line(current_line, current_file)