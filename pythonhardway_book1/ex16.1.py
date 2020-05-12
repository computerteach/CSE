from sys import argv
#this starts the file- to run must inssert program name and the new filename you are creating
script, filename = argv
print("We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# the above gets you going. If you choose CTL-C it shuts down - return gives the creation of the document 
input("?")
#the "w" below is the command to write
print("Opening the file...")
target = open(filename, 'w')
#cleans out the file for creation
print("Truncating the file. Goodbye!")
target.truncate()
#start the input piece for the lines
print("Now I am going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3:  ")
#this writes the file below sends it to the target of the prgram and moves down a line.
print("I'm going to write these to a file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#close the file
print("And finally we close it.")
target.close()
