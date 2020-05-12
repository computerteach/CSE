from sys import argv
from os.path import exists

script, from_file, to_file = argv

#this line isn't needed - print(f"Copying from {from_file} to {to_file}")

#doing it in one line, How?
in_file = open(from_file)
indata = in_file.read()

#this line isn't needed - print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTL-C to abort.")
input()

out_file = open(to_file, "w")
out_file.write(indata)

print("Alright, all done.")
out_file.close()
in_file.close()
